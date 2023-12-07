from django.shortcuts import render
from .models import productos

def lista_productos(request):
    lista_productos = productos.objects.all()
    
    return render(request, 'ventas.html', {'lista_productos': lista_productos})
