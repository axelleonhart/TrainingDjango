from apps.clientes.forms import ClienteForm
from apps.clientes.models import Cliente
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.


class ClientesList(ListView):
    """
    Crea una lista con todos los clientes dados de alta en el modelo
    """
    model = Cliente
    template_name = 'cliente/cliente_lista.html'


class ClientesCreate(CreateView):
    """
    Muestra un formulario para la creación de clientes
    """
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_listar')


class ClientesUpdate(UpdateView):
    """
    Muestra un formulario para la edición de clientes
    """
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_listar')


class ClienteDelete(DeleteView):
    """
    Se le pide al usuario se desea la eliminación de clientes
    """
    model = Cliente
    template_name = 'cliente/cliente_delete.html'
    success_url = reverse_lazy('cliente:cliente_listar')
