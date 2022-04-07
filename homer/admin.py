from cProfile import Profile
from django.contrib import admin
from .models import JobPost, Profile


@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['job_title']
    }
    list_display = ['job_title', 'job_confirm', ]


# admin.site.register(Profiles)
