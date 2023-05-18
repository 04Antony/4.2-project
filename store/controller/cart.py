from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from store.models import Product, Cart


def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
                prod_id = int(request.POST.get('product_id'))
                product_check = Product.objects.get(id=prod_id)
                if(product_check):
                    if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                         returnJsonResponse({'status':"Product already in Cart" })
                    else:
                        prod_qty = int(request.POST.get('product_qty'))
                        
                        if product_check.quantity >= prod_qty :
                            Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                            returnJsonResponse({'status':"Product added successfully" })
                        else:
                            returnJsonResponse({'status':"Only "+ str(product_check.quantity) + "quantity available" })
                else:
                    returnJsonResponse({'status': "No such product found" })
        else:
            returnJsonResponse({'status': "Login to continue" })

    return redirect('/')

def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render(request, "store/cart.html", context)

def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonRespose({'status: Updated successfully'})
    return redirect('/')

def deletecartitem(request):
     if request.method == 'POST':
         prod_id = int(request.POST.get('product_id'))
         if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cartitem = Cart.objects.get(product_id=prod_id, user=request.user)
            cartitem.delete()
         return JsonRespose({'status: Deleted successfully'})
     return redirect('/')





