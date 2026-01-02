from django.db import models


# Create your models here.
class contact_message(models.Model):
    c_auto_id = models.AutoField(primary_key=True)
    c_name = models.TextField(max_length=10)
    c_email = models.EmailField(max_length=20)
    c_message = models.TextField(max_length=100)
