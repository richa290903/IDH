from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from all_product.models import product 
from django.contrib import messages

def profile(request):
    return profile_page(request)


def profile_page(request):
    data = {
        'first_name': request.session.get('first_name'),
        'last_name': request.session.get('last_name'),
        'user_name': request.session.get('user_name'),
        'email': request.session.get('email'),
        'mobile_no': request.session.get('mobile_no'),
        'company_name': request.session.get('company_name'),
        'company_address': request.session.get('company_address'),
        'about_company': request.session.get('about_company'),
        'website_link': request.session.get('website_link'),
        'photo': request.session.get('photo'),
    }
    products_data = product.objects.all()

    context = {
        'data':data,
        'products_data': products_data
    }

    return render(request, "profile.html", context)


@ensure_csrf_cookie
def product_insert(request):
    try:
        if request.method == "POST":
            p_name = request.POST['p_name']
            p_image=request.FILES.get('p_image')
            p_keyword = request.POST['p_keyword']
            height = request.POST['height']
            width = request.POST['width']
            furniture_highlights = request.POST['furniture_highlights']
            wall_features = request.POST['wall_features']
            room_highlights = request.POST['room_highlights']
            lighting = request.POST['lighting']
            storage_features = request.POST['storage_features']
            unique_id = request.POST['unique_id']
            
            qry = product(p_name=p_name,p_image=p_image,p_keyword=p_keyword,height=height,width=width,furniture_highlights=furniture_highlights,wall_features=wall_features,room_highlights=room_highlights,lighting=lighting,storage_features=storage_features,unique_id=unique_id)
            qry.save()
            messages.success(request, 'Post uploaded successfully.')

    except Exception as e:
        messages.error(request, f"Post upload error: {e}")

    return render(request, "profile.html")



