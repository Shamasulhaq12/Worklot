from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

from rest_framework import serializers
from.models import Notification


User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    #

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'name',
                  'password', 'is_superuser', 'is_active', 'is_homer', 'fcm_token']


class NotificationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    user = serializers.StringRelatedField()
    # fcm_token = serializers.SerializerMethodField()
    # title = serializers.CharField(max_length=255)
    # description = serializers.CharField(max_length=255)
    # fcm_tokens = serializers.StringRelatedField()
    # fcm_list = serializers.SerializerMethodField()
    # # fcm_tokens = serializers.SerializerMethodField()

    # class Meta:
    #     model = Notification
    #     fields = '__all__'


# class FcmTokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FcmToken
#         fields = '__all__'
