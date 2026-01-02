from django.shortcuts import render
from django.templatetags.static import static

def home(request):
    images = [
        static('img1.jpg'),
        static('img2.jpg'),
        static('img3.jpg'),]
    
    return render(request,"home/home.html",{"images": images})


    