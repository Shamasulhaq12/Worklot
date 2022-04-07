from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('job/', views.JobPostListView.as_view()),
    path('job/<int:pk>', views.JobPostDetailView.as_view()),
    path('profile/<int:pk>', views.ProfileDetailView.as_view()),
    # path('upload/', views.file_upload),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
