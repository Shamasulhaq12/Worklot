from .models import JobBid, Portfolio, Government_details, Service
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class JobBidSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobBid
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class Government_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Government_details
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
