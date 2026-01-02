from django.contrib import admin
from .models import User, Designer


# Register your models here.

class user_Admin(admin.ModelAdmin):
    list_display = ('user_id', 'user_type', 'first_name', 'last_name', 'user_name', 'email', 'password', 'mobile_no', 'company_name', 'company_address', 'about_company', 'website_link')


admin.site.register(User, user_Admin)


class designer_Admin(admin.ModelAdmin):
    list_display = ('designer_id', 'user_type', 'first_name', 'last_name', 'user_name', 'email', 'password', 'mobile_no', 'company_name', 'company_address', 'about_company', 'website_link')


admin.site.register(Designer, designer_Admin)
