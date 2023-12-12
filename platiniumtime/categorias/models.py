from django.db import models
from ventas.models import Product
class Category(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    products = models.ManyToManyField(Product, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
