from django.db import IntegrityError
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import ModelSerializer, Serializer

from .models import User


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension,)

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class UserSerializer(ModelSerializer):
    avatar = Base64ImageField(
        max_length=None, use_url=True, allow_null=True, read_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'salutation', 'first_name', 'last_name', 'gender', 'mobile', 'avatar',
                  'date_joined']


class PasswordSerializer(Serializer):
    password = CharField(label=_("Password"), style={'input_type':'password'}, min_length=8, max_length=255)
    password_again = CharField(label=_("Password"), style={'input_type':'password'}, min_length=8, max_length=255)

    def validate(self, data):
        if data['password'] != data['password_again']:
            raise ValidationError("password and Password again Does not match")
        return data


class SignupSerializer(Serializer):
    username = CharField(max_length=255)
    email = EmailField(max_length=255)
    password = CharField(label=_("Password"), style={'input_type':'password'}, min_length=8, max_length=255)
    password_again = CharField(label=_("Password Again"), style={'input_type':'password'}, min_length=8,
                               max_length=255)

    class Meta:
        fields = ['username', 'email', 'password', 'password_again']
        extra_kwargs = {
            'password':{'write_only':True},
            'password_again':{'write_only':True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password_again')

        try:
            user = User.objects.create(**validated_data)
            user.set_password(password)
            user.save()
            return user
        except IntegrityError as e:
            raise ValidationError(
                {'non_field_errors':['Either Username or Email has been already Registered. Please try again']})

    def validate(self, attrs):
        password = attrs.get('password')
        password_again = attrs.get('password_again')
        if password != password_again:
            raise ValidationError('Password and Password Again does not match')
        return attrs

    def to_representation(self, instance):
        self._readable_fields.pop(-1)  # to remove password_again field after post
        self._readable_fields.pop(-1)  # to remove password field after post
        return super().to_representation(instance)
