from typing import Any
from django import http
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import ShippingAddress
from .forms import ShippingAddressForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit  import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404

class ShippingAddressListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = ShippingAddress
    template_name = 'shipping_addresses/shipping_addresses.html'

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')

class ShippingAddressUpadateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
      login_url = 'login'
      model = ShippingAddress
      form_class = ShippingAddressForm
      template_name ='shipping_addresses/update.html'
      success_message = 'Direccion actualizada exitosamente'
      
      def get_success_url(self):
        return reverse('shipping_addresses:shipping_addresses')
      def dispatch(self, request, *args, **kwargs):
          if request.user.id != self.get_object().user_id:
              return redirect ('carts:cart')
          return super(ShippingAddressUpadateView, self).dispatch(request, *args, **kwargs)

class ShippingAddressDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login',
    model = ShippingAddress
    template_name ='shipping_addresses/delete.html'
    success_url = reverse_lazy('shipping_addresses:shipping_addresses')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().default:
            return redirect('shipping_addresses:shipping_addresses')
        if request.user.id != self.get_object().user_id:
              return redirect ('carts:cart')
        return super(ShippingAddressDeleteView, self).dispatch(request, *args, **kwargs)
@login_required(login_url='login')
def create(request):
    form = ShippingAddressForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        shipping_address = form.save(commit=False)
        shipping_address.user = request.user
        shipping_address.default = not ShippingAddress.objects.filter(user=request.user).exists()

        shipping_address.save()

        messages.success(request, 'Direccion creada exitosamente')
        return redirect('shipping_addresses:shipping_addresses')

    return render(request, 'shipping_addresses/create.html',{
        'form': form
    })

@login_required(login_url='login')
def default(request, pk):
    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user.id:
        return redirect('carts:cart')
    
    if request.user.shippingaddress_set.filter(default=True).exists():
        request.user.shippingaddress_set.update(default=False)

    shipping_address.default = True
    shipping_address.save()
    
    return redirect('shipping_addresses:shipping_addresses')