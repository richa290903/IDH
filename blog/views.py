from django.shortcuts import render
from .models import Blog
from django.contrib import messages


def blog(request):
     blog_data = Blog.objects.all()
    
     return render(request, "blog.html",{"blog_data":blog_data})


def upload_blog(request):
    try:
        if request.method == "POST":
            blog_title = request.POST['blog_title']
            blog_img = Blog(request.POST, request.FILES)
            blog_img = request.FILES.get('blog_img')
            blog_description = request.POST['blog_description']
            qry = Blog(blog_title=blog_title, blog_img=blog_img, blog_description=blog_description)
            qry.save()
            messages.success(request, 'Blog inserted successfully.')

    except Exception as e:
        messages.error(request, f"Blog Insert error: {e}")

    return render(request, "blog.html")

    