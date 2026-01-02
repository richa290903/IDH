from django.contrib import admin
from .models import Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_id', 'blog_title', 'blog_img', 'blog_description')


admin.site.register(Blog, BlogAdmin)
