from django.db import models


class product(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.TextField(max_length=50)
    p_image = models.FileField(upload_to="all_product/", max_length=250, null=True, default=None)
    p_keyword = models.TextField(max_length=255)
    height = models.CharField(max_length=20)
    width = models.CharField(max_length=20)
    furniture_highlights = models.TextField(max_length=255)
    wall_features = models.TextField(max_length=255)
    room_highlights = models.TextField(max_length=255)
    lighting = models.TextField(max_length=255)
    storage_features = models.TextField(max_length=255)
    unique_id = models.CharField(max_length=20)


