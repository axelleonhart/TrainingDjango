from apps.proveedores.forms import ProveedorForm
from apps.proveedores.models import Proveedor
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.


class ProveedorList(ListView):
    model = Proveedor
    template_name = 'proveedor/proveedor_lista.html'


class ProveedorUpdate(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor:proveedor_listar')


class ProveedorCreate(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor:proveedor_listar')


class ProveedorDelete(DeleteView):
    model = Proveedor
    template_name = 'proveedor/proveedor_delete.html'
    success_url = reverse_lazy('proveedor:proveedor_listar')
