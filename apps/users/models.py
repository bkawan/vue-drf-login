from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.core.utils import get_image_path


# Create your models here.

class User(AbstractUser):
    USER_STATUS_CHOICES = (
        ('Approved', 'Approved'),
        ('Blocked', 'Blocked'),
        ('Pending', 'Pending'),
        ('Registered', 'Registered'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    SALUTATION = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Sir', 'Sir'),
        ('Mx', 'Mx'),
        ('Other', 'Other'),
    )
    salutation = models.CharField(choices=SALUTATION, max_length=255)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=15)
    status = models.CharField(choices=USER_STATUS_CHOICES, max_length=30, default='Registered')
    avatar = models.ImageField(upload_to=get_image_path, null=True, blank=True)

    def __str__(self):
        return '{}-{}-{} {}'.format(self.username, self.email, self.first_name, self.last_name)
