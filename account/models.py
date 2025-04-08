from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
# Create your models here.


class CustomUser(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is a required field')

        email = self.normalize_email(email=email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff set to True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser set to True')

        return self.create_user(email=email, password=password, **extra_fields)


USER_TYPE_CHOICES = (
    ('POST_JOB', 'recruiter'),
    ('APPLY_JOB', 'applicant'),
)

def generate_api_key():
    return str(uuid.uuid4())

class UserModel(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True)
    user_img = models.ImageField(upload_to='profile_img/',blank=True, null=True)
    user_type = models.CharField(choices=USER_TYPE_CHOICES, default='applicant')
    api_key = models.CharField(default=generate_api_key, unique=True)
    resume = models.FileField(upload_to='resumes', null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    joined_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = CustomUser()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
