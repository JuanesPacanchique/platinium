from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product

class ProductListView(ListView):

    template_name = 'productos.html'
    model= Product
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'productos/detalle.html'   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        
        return context