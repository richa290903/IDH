from django.shortcuts import render

def change_password(request):
    return render(request,"change_password.html")
