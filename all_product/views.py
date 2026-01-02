from django.shortcuts import render
from django.contrib import messages
from .models import product


def all_product(request):
     product_data = product.objects.all()[:9]
    
     return render(request, "all_product.html",{"products_data":product_data})



def search_data(request):
    try:
        search = request.GET.get('search', '').strip()

        if search:
            product_data = product.objects.filter(p_keyword__icontains=search)
        else:
            product_data = product.objects.all()

    except Exception as e:
        messages.error(request, f"Error occurred: {e}")
        product_data = product.objects.none()

    return render(request, "all_product.html", {'products_data': product_data})
