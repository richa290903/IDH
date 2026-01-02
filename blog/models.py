from django.db import models

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.TextField(max_length=100)
    blog_img = models.FileField(upload_to="blog/", max_length=250, null=True, default=None)
    blog_description = models.TextField(max_length=1000)
