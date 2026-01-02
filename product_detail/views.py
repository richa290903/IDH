from django.shortcuts import render,get_object_or_404
from all_product.models import product
from registration_form.models import Designer
from django.contrib import messages


def product_detail(request, id):
    product_data = {}
    try:
        product_data = get_object_or_404(product, p_id=id)

        product_data.save()
        messages.success(request, " Single Data fetched Successfully")
    except Exception as e:
        messages.error(request, f"Single Data fetched error:{e}")


    user_data = Designer.objects.all()
    context = {
        'data':product_data,
        'user_data':user_data
    }
    return render(request, "product_detail.html",context)

# def post_user_fetch(request):
#     user_data = {}
#     try:
#             user_data = Designer.objects.all()
#     except Exception as e:
#         messages.error(request,f"User data fetch error:{e}")
    
#     return render(request,"product_detail.html",{'user_data':user_data})

