from django.conf.urls import url
from apps.proveedores.views import ProveedorList, ProveedorUpdate, \
                                   ProveedorCreate, ProveedorDelete

urlpatterns = [
    url(r'^listar/', ProveedorList.as_view(), name="proveedor_listar"),
    url(r'^editar/(?P<pk>\w+)/$', ProveedorUpdate.as_view(),
        name="proveedor_editar"),
    url(r'^nuevo/$', ProveedorCreate.as_view(), name="proveedor_crear"),
    url(r'^eliminar/(?P<pk>\w+)/$', ProveedorDelete.as_view(),
        name="proveedor_eliminar"),
]
