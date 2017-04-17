from django.conf.urls import url
from apps.contratos.views import ContratoList, ContratoCreate, \
                                 ContratoUpdate, ContratoDelete

urlpatterns = [
    url(r'^listar/$', ContratoList.as_view(), name='contrato_listar'),
    url(r'^crear/', ContratoCreate.as_view(), name="contrato_crear"),
    url(r'^editar/(?P<pk>\w+)/$', ContratoUpdate.as_view(),
        name='contrato_editar'),
    url(r'^eliminar/(?P<pk>\w+)/$', ContratoDelete.as_view(),
        name='contrato_eliminar'),
]
