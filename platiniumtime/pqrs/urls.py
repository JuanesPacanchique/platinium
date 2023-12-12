from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('crear_pqrs/', views.crear_pqrs, name='crear_pqrs'),
]