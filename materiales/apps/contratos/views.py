from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.contratos.forms import ContratoForm
from apps.contratos.models import Contrato, Proveedor
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import time
# Create your views here.


class ContratoList(ListView):
	model = Contrato
	template_name = 'contrato/contrato_lista.html'


class ContratoCreate(CreateView):
	model = Contrato
	form_class = ContratoForm
	template_name = 'contrato/contrato_form.html'
	success_url = reverse_lazy('contrato:contrato_listar')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		solicitud = form.save(commit=False)
		solicitud.fecha = time.strftime("%Y-%m-%d")
		solicitud.save()
		return HttpResponseRedirect(self.get_success_url())