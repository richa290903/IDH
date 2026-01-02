from django.shortcuts import render
from registration_form.models import User, Designer
from django.contrib import messages


def login(request):
    return render(request, "login.html")


def login_register(request):
    try:
        if request.method == "POST":
            e = request.POST['email']
            p = request.POST['password']

            
            user = User.objects.filter(email=e, password=p).first()
            if user:
                request.session.flush()
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                request.session['user_name'] = user.user_name
                request.session['email'] = user.email
                request.session['mobile_no'] = user.mobile_no
                request.session['company_name'] = user.company_name
                request.session['company_address'] = user.company_address
                request.session['about_company'] = user.about_company
                request.session['website_link'] = user.website_link
                request.session['photo'] = user.photo.name
                messages.success(request, "User Found.")
                return render(request, "home/home.html")  

           
            designer = Designer.objects.filter(email=e, password=p).first()
            if designer:
                request.session.flush()
                request.session['first_name'] = designer.first_name
                request.session['last_name'] = designer.last_name
                request.session['user_name'] = designer.user_name
                request.session['email'] = designer.email
                request.session['mobile_no'] = designer.mobile_no
                request.session['company_name'] = designer.company_name
                request.session['company_address'] = designer.company_address
                request.session['about_company'] = designer.about_company
                request.session['website_link'] = designer.website_link
                request.session['photo'] = designer.photo.name
                messages.success(request, "Designer Found.")
                return render(request, "home/home.html")  

            
            messages.error(request, "User not Found.")
    except Exception as err:
        messages.error(request, f"Error occurred: {err}")

    return render(request, "login.html")
