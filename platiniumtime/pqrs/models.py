from django.db import models
from django.contrib.auth.models import User  # Importa el modelo de usuario de Django si aún no lo has hecho

class PQRS(models.Model):
    OPCIONES_PQRS = [
        ('pregunta', 'Pregunta'),
        ('queja', 'Queja'),
        ('reclamo', 'Reclamo'),
        ('sugerencia', 'Sugerencia'),
    ]

    opcion = models.CharField(max_length=20, choices=OPCIONES_PQRS, null=True)
    texto = models.TextField()
    correo = models.EmailField(null=True, blank=True)  

    def __str__(self):
        return f"{self.get_opcion_display()}: {self.texto}"
