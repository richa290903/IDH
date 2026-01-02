from django.contrib import admin
from .models import contact_message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('c_auto_id', 'c_name', 'c_email', 'c_message')


admin.site.register(contact_message, MessageAdmin)

