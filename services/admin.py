from django.contrib import admin
from .models import JobBid, Government_details, Portfolio, Service

admin.site.register(JobBid)
admin.site.register(Government_details)
admin.site.register(Portfolio)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
