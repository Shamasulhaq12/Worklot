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


class ServiceEnum(models.IntegerChoices):
    ONE = 1, 'Web developer'
    TWO = 2, 'SEO Expert'
    THREE = 3, 'Mobile Apps Developments'
    FOUR = 4, 'Graphic Designer'
    FIVE = 5, 'Manager'


class Images(models.Model):
    image_frontside = models.ImageField(
        upload_to='images/Nationaldetails/image_frontside')
    image_backside = models.ImageField(
        upload_to='images/Nationaldetails/image_backside')


class JobBid(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)
    massege = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    job_budgets = models.IntegerField(null=True, blank=True)
    buget = models.IntegerField(null=True, blank=True, default=5)


class Government_details(models.Model):
    name = models.OneToOneField(
        User, related_name="Government", on_delete=models.CASCADE)
    id_card_Num = models.CharField(
        max_length=15, help_text="xxxxx-xxxxxxx-x", unique=True)
    image_frontside = models.ImageField(
        upload_to='images/Nationaldetails/image_frontside', blank=True)
    image_backside = models.ImageField(
        upload_to='images/Nationaldetails/image_backside', blank=True)


class Portfolio(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="portfolio")
    # Service = models.IntegerField(choices=ServiceEnum.choices)
    about_me = models.TextField()
    service = models.IntegerField(choices=ServiceEnum.choices)
    images = models.ImageField(
        upload_to='images/portfolio', default='', null=False)


class Service(models.Model):
    title = models.CharField(max_length=255)
