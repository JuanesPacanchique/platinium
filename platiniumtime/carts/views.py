from django.shortcuts import render, redirect
from .models import Cart
from django.urls import reverse
from .utils import get_or_create_cart
from ventas.models import Product
from .models import CartProducts
from django.shortcuts import get_object_or_404

def cart(request):
    cart = get_or_create_cart(request)
    products = cart.products.all()  # Obtener todos los productos del carrito

    return render(request, 'carts/cart.html', {'cart': cart, 'products': products})

def add(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))

    #product = get_object_or_404(Product, pk=product_id)
    #cart.products.add(product, through_defaults={
    #   'quantity' :  quantity
    #})
     
    cart_product = CartProducts.objects.create_or_update_quantity(cart=cart, product=product, quantity=quantity)

    return render(request, 'carts/add.html', {
        'quantity': quantity, 
        'cart_product': cart_product,
        'product': product
    })

def remove(request):
    cart = get_or_create_cart(request)
    product_id = request.POST.get('product_id')

    product = get_object_or_404(Product, pk=product_id)
    if product in cart.products.all():
        cart.products.remove(product)

    return redirect('carts:cart')

