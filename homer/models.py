# from .models import JobPostImage
from re import I
from time import time
from os import name
from tkinter.tix import STATUS
from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.exceptions import ValidationError
User = get_user_model()
# Create your models here.


class ServiceEnum(models.IntegerChoices):
    ONE = 1, 'Web developer'
    TWO = 2, 'SEO Expert'
    THREE = 3, 'Mobile Apps Developments'
    FOUR = 4, 'Graphic Designer'
    FIVE = 5, 'Manager'


class StatusEnum(models.IntegerChoices):
    ONE = 1, 'Not Assign'
    TWO = 2, 'Assign'
    THREE = 3, 'Confirmed'
    FOUR = 4, 'Done'


class Images(models.Model):
    image = models.ImageField(upload_to='images/image')

    # def clean(self):
    #     duplicate = Service.objects.exclude(pk=self.pk).filter(
    #         user_id=self.user_id, service_id=self.service_id
    #     ).exists()
    #     if duplicate:
    #         raise ValidationError(
    #             'The service with this user already exists')
    #     return super().clean()


class JobPost(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    # job_services = models.ForeignKey(
    #     choices=Service.objects.all(), on_delete=models.CASCADE)
    buget = models.IntegerField(default=0)
    deadline = models.DateTimeField(default=timezone.now)
    massege = models.TextField(max_length=255, blank=True)
    address = models.CharField(max_length=255)

    created_date = models.DateTimeField(default=timezone.now)
    job_status = models.IntegerField(choices=StatusEnum.choices)
    job_done = models.BooleanField(default=False)
    job_confirm = models.BooleanField(default=True)
    payment = models.BooleanField(default=False)
    images = models.FileField()
    images = models.FileField()

    def __int__(self):
        return self.job_title

    class Meta:
        verbose_name = 'Jobs'


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    # Service = models.IntegerField(choices=ServiceEnum.choices)
    about_me = models.TextField()
    images = models.ImageField(
        upload_to='images/profile', default='', null=False)


# class PostImage(models.Model):
#     post_images = models.OneToOneField(
#         image, on_delete=models.CASCADE, )
#     post = models.ForeignKey(JobPost, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.jobpost.username
