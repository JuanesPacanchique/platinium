from django.shortcuts import render
from django.http import HttpResponse
from .models import PQRS

def guardar_pqrs(request):
    if request.method == 'POST':
        pqrs_texto = request.POST.get('pqrs') 
        nueva_pqrs = PQRS.objects.create(texto=pqrs_texto)
        return HttpResponse("PQRS enviada exitosamente")
        

    return render(request, 'pqrs.html') 

