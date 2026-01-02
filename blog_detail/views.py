from django.shortcuts import render,get_object_or_404
from blog.models import Blog
from django.contrib import messages


def blog_detail(request, id):
    blog_data = {}
    try:
        blog_data = get_object_or_404(Blog, blog_id=id)
        blog_data.save()
        messages.success(request, "Single Data fetched Successfully")
    except Exception as e:
        messages.error(request, f"Single Data fetched error:{e}")

    return render(request, "blog_detail.html",{'data':blog_data})

