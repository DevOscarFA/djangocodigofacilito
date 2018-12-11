from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.adopcion.views import index, PersonaList, PersonaCrate, PersonaUpdate, PersonaDelete, SolicitidListar, \
    SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    url(r'^$', index),
    url(r'^listar$', login_required(PersonaList.as_view()), name='adopcion_listar'),
    url(r'^crear$', login_required(PersonaCrate.as_view()), name='adopcion_crear'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(PersonaUpdate.as_view()), name='adopcion_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(PersonaDelete.as_view()), name='adopcion_eliminar'),
    url(r'^solicitud/listar$', login_required(SolicitidListar.as_view()), name='solicitud_listar'),
    url(r'^solicitud/crear$', login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
    url(r'^solicitud/editar/(?P<pk>\d+)/$', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
    url(r'^solicitud/eliminar/(?P<pk>\d+)/$', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),
]