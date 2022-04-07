from django.contrib import admin
from .models import User, Notification

# Register your models here.
# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_active',
                    'is_staff', 'is_superuser', 'fcm_token']
    list_editable = ['is_staff', 'is_superuser']
    readonly_fields = ['is_staff', 'is_homer']

# admin.site.register(FcmToken)


# @admin.register(Notes)
# class NotesAdmin(admin.ModelAdmin):
#     prepopulated_fields = {
#         'slug': ['title']
#     }
#     list_display = ['title', 'slug', 'created_at', 'updated_at', 'is_active']
#     list_editable = ['is_active']
admin.site.register(Notification)
