from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('bid/', views.JobBidListView.as_view()),
    path('bid/<int:id>', views.JobBidView.as_view()),
    path('portfolio/<int:id>', views.WorkerPortfolioListView.as_view()),
    path('portfolio/', views.WorkerPortfolioView.as_view()),
    path('gov/<int:pk>', views.Government_detailsView.as_view()),
    path('gov/', views.Government_detailsList.as_view()),
    path('services', views.ServiceViews.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = format_suffix_patterns(urlpatterns)
