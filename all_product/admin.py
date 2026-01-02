from django.contrib import admin
from .models import product


class productAdmin(admin.ModelAdmin):
    list_display = (
        'p_id', 'p_name', 'p_image', 'p_keyword', 'height', 'width', 'furniture_highlights', 'wall_features',
        'room_highlights', 'lighting', 'storage_features', 'unique_id')


admin.site.register(product, productAdmin)
