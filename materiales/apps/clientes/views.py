from django.shortcuts import render
from django.http import HttpResponse
from apps.clientes.forms import ClienteForm
from apps.clientes.models import Cliente
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class ClientesList(ListView):
	model = Cliente
	template_name = 'cliente/cliente_lista.html'

class ClientesCreate(CreateView):
	model = Cliente
	form_class = ClienteForm
	template_name = 'cliente/cliente_form.html'
	success_url = reverse_lazy('cliente:cliente_listar')

class ClientesUpdate(UpdateView):
	model = Cliente
	form_class = ClienteForm
	template_name = 'cliente/cliente_form.html'
	success_url = reverse_lazy('cliente:cliente_listar')

class ClienteDelete(DeleteView):
	model = Cliente
	template_name = 'cliente/cliente_delete.html'
	success_url = reverse_lazy('cliente:cliente_listar')