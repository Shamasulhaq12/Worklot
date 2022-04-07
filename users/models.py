from tkinter.messagebox import NO
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from rest_framework.response import Response
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None, fcm_token=None):
        if not email:
            raise ValueError(
                {'error': 'something went wrong while getting profile'})
        print(email)
        # if '@gmail' in email:
        #     raise Response(
        #         {'error': 'something went wrong while getting profile'})
        user = self.model(email=self.normalize_email(
            email), name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password=None, fcm_token=None):
        if password is None:
            raise TypeError("user must have an password")
        user = self.create_user(email, name, password, fcm_token)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100,)
    is_staff = models.BooleanField(default=False)
    is_homer = models.BooleanField(default=True)
    fcm_token = models.CharField(max_length=255, blank=True, null=True)
    # is_login = models.BooleanField(default=False)
    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'fcm_token']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __int__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_fcm_token(self):
        return self.fcm_token


class Profiles(models.Model):
    image = models.ImageField(
        upload_to='image/profiles/', blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)


# Model to store the list of logged in users


class LoggedInUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='logged_in_user')
    # Session keys are 32 characters long
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username


# class FcmToken(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE)
#     fcm_tokens = models.CharField(max_length=255)

#     def __str__(self):
#         return self.fcm_tokens


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(max_length=255)
    is_read = models.BooleanField(default=False)
    # fcm_token = models.ForeignKey(User, on_delete=models.CASCADE)

    # def fcm_list(self):
    #     return self.fcm_token.all()

    def __str__(self):
        return self.title + '|' + self.user.fcm_token
