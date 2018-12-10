from django.conf.urls import url

from apps.adopcion.views import index, PersonaList, PersonaCrate, PersonaUpdate, PersonaDelete, SolicitidListar, \
    SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    url(r'^$', index),
    url(r'^listar$', PersonaList.as_view(), name='adopcion_listar'),
    url(r'^crear$', PersonaCrate.as_view(), name='adopcion_crear'),
    url(r'^editar/(?P<pk>\d+)/$', PersonaUpdate.as_view(), name='adopcion_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', PersonaDelete.as_view(), name='adopcion_eliminar'),
    url(r'^solicitud/listar$', SolicitidListar.as_view(), name='solicitud_listar'),
    url(r'^solicitud/crear$', SolicitudCreate.as_view(), name='solicitud_crear'),
    url(r'^solicitud/editar/(?P<pk>\d+)/$', SolicitudUpdate.as_view(), name='solicitud_editar'),
    url(r'^solicitud/eliminar/(?P<pk>\d+)/$', SolicitudDelete.as_view(), name='solicitud_eliminar'),
]