from apps.proveedores.forms import ProveedorForm
from apps.proveedores.models import Proveedor
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.


class ProveedorList(ListView):
    """
    Crea una lista con todos los proveedores dados de alta en el modelo
    """
    model = Proveedor
    template_name = 'proveedor/proveedor_lista.html'


class ProveedorUpdate(UpdateView):
    """
    Muestra un formulario para la edición de proveedores
    """
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor:proveedor_listar')


class ProveedorCreate(CreateView):
    """
    Muestra un formulario para la creación de proveedores
    """
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor:proveedor_listar')


class ProveedorDelete(DeleteView):
    """
    Se le pide al usuario se desea la eliminación de proveedores
    """
    model = Proveedor
    template_name = 'proveedor/proveedor_delete.html'
    success_url = reverse_lazy('proveedor:proveedor_listar')
