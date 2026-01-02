"""IDH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import home
from contact.views import contact,insert_msg
from all_product.views import all_product,search_data
from blog.views import blog,upload_blog
from product_detail.views import product_detail
from blog_detail.views import blog_detail
from login.views import login,login_register
from change_password.views import change_password
from forgot_password.views import forgot_password
from registration_form.views import registration_form,register
from profile1.views import profile,profile_page,product_insert


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('contact/',contact,name="contact"),
    path('all_product/',all_product,name="all_product"),
    path('blog/',blog,name="blog"),
    path('product_detail/<int:id>/',product_detail,name="product_detail"),
    path('blog_detail/<int:id>/',blog_detail,name="blog_detail"),
    path('login/',login,name="login"),
    path('change_password/',change_password,name="change_password"),
    path('forgot_password/', forgot_password, name="forgot_password"),
    path('registration_form/',registration_form,name="registration_form"),
    path('insert_msg/',insert_msg,name="insert_msg"),
    path('upload_blog/',upload_blog,name="upload_blog"),
    path('register/',register,name="register"),
    path('login_register/',login_register,name="login_register"),
    path('search_data/',search_data,name="search_data"),
    path('profile/',profile,name="profile"),
    path('profile_page/',profile_page,name="profile_page"),
    path('product_insert/',product_insert,name="product_insert"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)