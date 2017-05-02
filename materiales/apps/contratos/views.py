from django.http import HttpResponseRedirect
from apps.contratos.forms import ContratoForm
from apps.contratos.models import Contrato
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import time
# Create your views here.


class ContratoList(ListView):
    """
    Crea una lista con todos los contratos dados de alta en el modelo
    """
    model = Contrato
    template_name = 'contrato/contrato_lista.html'


class ContratoCreate(CreateView):
    """
    Muestra un formulario para la creación de contratos
    """
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


class ContratoUpdate(UpdateView):
    """
    Muestra un formulario para la edición de contratos
    """
    model = Contrato
    form_class = ContratoForm
    template_name = 'contrato/contrato_form.html'
    success_url = reverse_lazy('contrato:contrato_listar')


class ContratoDelete(DeleteView):
    """
    Se le pide al usuario se desea la eliminación de contratos
    """
    model = Contrato
    template_name = 'contrato/contrato_delete.html'
    success_url = reverse_lazy('contrato:contrato_listar')
