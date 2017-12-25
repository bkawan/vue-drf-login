from django.utils.translation import ugettext as _
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PasswordSerializer(Serializer):
    password = CharField(label=_("Password"), style={'input_type': 'password'}, min_length=8, max_length=255)
    password_again = CharField(label=_("Password"), style={'input_type': 'password'}, min_length=8, max_length=255)

    def validate(self, data):
        if data['password'] != data['password_again']:
            raise ValidationError("password and Password again Does not match")
        return data
