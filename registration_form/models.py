from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_type = models.TextField(max_length=20)
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=100)
    user_name = models.TextField(max_length=10, unique=True)
    email = models.EmailField()
    password = models.TextField(max_length=True, unique=True)
    mobile_no = models.CharField(max_length=12)
    company_name = models.TextField(max_length=20)
    company_address = models.TextField(max_length=100)
    about_company = models.TextField(max_length=500)
    website_link = models.TextField(max_length=100)
    photo=models.FileField(upload_to="user/",max_length=250,null=True,default=None)


class Designer(models.Model):
    designer_id = models.AutoField(primary_key=True)
    user_type = models.TextField(max_length=20)
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=100)
    user_name = models.TextField(max_length=10, unique=True)
    email = models.EmailField()
    password = models.TextField(max_length=True, unique=True)
    mobile_no = models.CharField(max_length=12)
    company_name = models.TextField(max_length=20)
    company_address = models.TextField(max_length=100)
    about_company = models.TextField(max_length=500)
    website_link = models.TextField(max_length=100)
    photo=models.FileField(upload_to="designer/",max_length=250,null=True,default=None)
