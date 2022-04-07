# from rest_framework import routers
from django.urls import path, include

# from users.models import FcmToken
from .views import CustomerView, NotificationView, NotificationCreateApiView
from django.contrib import admin
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register('notify', NotificationView basename='notification')

# router = routers.SimpleRouter()
# router.register(r'users', UserViewSet)
# router.register(r'accounts', AccountViewSet)
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    # path('', include('router.urls')),
    path('profile', CustomerView.as_view()),
    path('notify/', NotificationView.as_view()),
    path('notify1/', NotificationCreateApiView.as_view()),
    # path('addfcmtoken/', FcmTokenPost.as_view())


]
# urlpatterns = router.urls
