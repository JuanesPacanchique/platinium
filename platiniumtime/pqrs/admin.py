from django.contrib import admin
from .models import PQRS

@admin.register(PQRS)
class PQRSAdmin(admin.ModelAdmin):
    list_display = ('texto', 'opcion',)

