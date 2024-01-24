from django.contrib import admin

from apps.drf_registration.models import CustomUser
from django.contrib.auth.admin import UserAdmin



# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id','first_name','last_name','username','email','role','is_active','is_staff','is_superuser','date_joined']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('role','image')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
            (None, {'fields': ('role','first_name','email')}),
    )

admin.site.register(CustomUser,CustomUserAdmin)
