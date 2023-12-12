from django.shortcuts import render,redirect

from .utils import breadcrumb
from .utils import get_or_create_order
from carts.utils import get_or_create_cart

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def order(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)
    if  not cart.has_products():
        return redirect('carts:cart')

    total_order = cart.total + order.shipping_total if order else cart.total

    return render(request, 'orders/order.html', {
        'cart': cart,
        'order': order,
        'total_order': total_order ,
        'breadcrumb' : breadcrumb()
    })

@login_required(login_url='login')
def address(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    return render(request, 'orders/address.html',{
        'cart': cart,
        'order': order,
    })
