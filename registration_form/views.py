from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .models import User, Designer


def registration_form(request):
    return render(request, "registration_form.html")


def register(request):
    try:
        if request.method == "POST":
            user_type = request.POST['user_type']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user_name = request.POST['user_name']
            photo = request.FILES['photo']
            email = request.POST['email']
            password = request.POST['password']
            mobile_no = request.POST['mobile_no']
            company_name = request.POST['company_name']
            company_address = request.POST['company_address']
            about_company = request.POST['about_company']
            website_link = request.POST['website_link']
            if user_type == "user":
                user = User(user_type=user_type,first_name=first_name,last_name=last_name,
                photo=photo,user_name=user_name,email=email,password=password,mobile_no=mobile_no,
                company_name=company_name,company_address=company_address,about_company=about_company,
                website_link=website_link)
                user.save()
                messages.success(request, 'User Data inserted successfully.')
                

                messages.success(request,"Session set for User")

            if user_type == "interior_designer":
                designer = Designer(user_type=user_type, first_name=first_name, last_name=last_name,
                                    photo=photo, user_name=user_name,email=email, password=password,
                                    mobile_no=mobile_no,company_name=company_name,
                                    company_address=company_address,about_company=about_company, website_link=website_link)
                designer.save()
                messages.success(request, 'Interior Designer Data inserted successfully.')

                
                messages.success(request,"Session set for Designer")

    except Exception as e:
        messages.error(request, f"Data Insert error: {e}")

    return render(request, "login.html")


