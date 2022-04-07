
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# from django.urls import path
# from basic_app import views

schema_view = get_schema_view(
    openapi.Info(
        title="workloat API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),

    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('services.urls')),
    path('homer/', include('homer.urls')),
    path('user/', include('users.urls')),
    path('auth/', include('djoser.urls')),
    path('accounts/login/', admin.site.urls),
    path('accounts/logout/', admin.site.logout),
    # path('admin/', admin.site.urls),
    # path('', views.login_redirect, name='login_redirect'),
    # path('accounts/login/', admin.site.urls),
    # path('accounts/logout/', admin.site.urls),
    # path('services/', include('services.urls')),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
    path('__debug__/', include('debug_toolbar.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
