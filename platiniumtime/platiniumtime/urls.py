"""
URL configuration for platiniumtime project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views
from ventas.views import ProductListView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('ventas/', ProductListView.as_view(), name='ventas'),
    path('', views.principal, name='principal'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registro_view, name='register'),
    path('pqrs/', views.pqrs, name='pqrs'),
    path('garantias/', views.garantias, name='garantias'),
    path('mantenimiento/', views.mantenimiento, name='mantenimiento'),
    path('admin/', admin.site.urls),
    path('producto/', include('ventas.urls')),
    path('carrito/', include('carts.urls')),
    path('orden/', include('orders.urls')),
    path('direcciones/', include('shipping_addresses.urls'))
] 

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)