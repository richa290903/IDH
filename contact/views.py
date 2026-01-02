from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import contact_message


def contact(request):
    return render(request, "contact.html")


def insert_msg(request):
    try:
        if request.method == "POST":
            c_name = request.POST['c_name']
            c_email = request.POST['c_email']
            c_message = request.POST['c_message']
            query = contact_message(c_name=c_name, c_email=c_email, c_message=c_message)
            query.save()
            messages.success(request, 'Data inserted successfully.')

    except Exception as e:
        messages.error(request, f"Data Insert error: {e}")

    return render(request, "contact.html")
