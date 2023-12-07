from django.contrib import admin
from django.db import models

class productos(models.Model):
    N_Producto = models.CharField(max_length=6)
    Descripcion = models.TextField(max_length=2000)
    Imagen = models.ImageField(upload_to='photo/%Y/%m/%d', null=True, blank=True)
    Precio = models.DecimalField(max_digits=8, decimal_places=3) 

    def __str__(self):
        return self.N_Producto 
