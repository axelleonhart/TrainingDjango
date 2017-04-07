from django.conf.urls import url
from apps.contratos.views import ContratoList, ContratoCreate

urlpatterns = [
	url(r'^listar/$', ContratoList.as_view(), name='contrato_listar'),
    url(r'^crear/', ContratoCreate.as_view(), name="contrato_crear"),
]