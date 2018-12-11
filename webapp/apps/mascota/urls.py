from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, listado

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(mascota_view), name='mascota_crear'),
    url(r'^listar$', login_required(mascota_list), name='mascota_listar'),
    url(r'^editar/(?P<id_mascota>\d+)$', login_required(mascota_edit), name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)$', login_required(mascota_delete), name='mascota_eliminar'),
    url(r'^listado', login_required(listado), name='listado'),
]
