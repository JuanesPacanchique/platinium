from django.shortcuts import render, redirect
from .models import PQRS
from pqrs.forms import Formulariopqrs
from django.contrib import messages

def crear_pqrs(request):
    if request.method == "POST":
        form = Formulariopqrs(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor_id = request.user.id
            post.correo = request.user.email
            post.save()
            messages.success(request, "La PQRS se ha enviado correctamente")
            return redirect("principal")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = Formulariopqrs()
    
    return render(request, "pqrs.html", {"form": form})


