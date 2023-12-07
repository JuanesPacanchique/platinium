from django.shortcuts import render
from django.shortcuts import redirect
from . import views
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm
from ventas.models import productos

from django.contrib.auth.models import User

def principal(request):
    return render(request,'principal.html',{
        #context
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password) 
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('principal')
        else: 
            messages.error(request, 'Usuario o contraseña no validos')
    return render (request, 'login.html', {
        
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')

def registro_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
    
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('principal')

    return render(request, 'register.html', {
        'form': form
    })

def ventas(request):
    return render(request,'ventas.html',{
        #context
    })

def pqrs(request):
    return render(request,'pqrs.html',{
        #context
    })

def garantias(request):
    return render(request,'Garantias.html',{
        #context
    })

def mantenimiento(request):
    return render(request,'mantenimiento.html',{
        #context
    })


def vista_tus_productos(request):
    # Obtener los últimos 5 productos añadidos, por ejemplo
    nuevos_productos = productos.objects.order_by('-fecha_creacion')[:5]

    # Luego, pasa estos productos a tu plantilla para mostrarlos
    return render(request, 'ventas.html', {'nuevos_productos': nuevos_productos})

