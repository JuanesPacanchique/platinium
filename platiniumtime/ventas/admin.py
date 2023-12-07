from django.contrib import admin
from .models import productos

@admin.register(productos)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['N_Producto', 'Descripcion', 'Imagen', 'Precio' ]
