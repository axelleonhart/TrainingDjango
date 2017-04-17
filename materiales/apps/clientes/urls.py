from django.conf.urls import url
from apps.clientes.views import ClientesList, ClientesCreate, \
                                ClientesUpdate, ClienteDelete

urlpatterns = [
    url(r'^listar/', ClientesList.as_view(), name="cliente_listar"),
    url(r'^crear/', ClientesCreate.as_view(), name="cliente_crear"),
    url(r'^editar/(?P<pk>\d+)$', ClientesUpdate.as_view(),
        name="cliente_editar"),
    url(r'^eliminar/(?P<pk>\d+)$', ClienteDelete.as_view(),
        name="cliente_eliminar"),
]
