from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required


urlpatterns = [

    # listar las carreras de la bd
    path('listarPorticos', views.listar_porticos, name="listar_porticos"),
    path('listarBicicletas', views.listar_bicicletas, name="listar_bicicletas"),

    
    # agregar un portico
    path('agregar_portico', views.agregar_portico, name="agregar_portico"),

    # editar un portico
    path('editar_portico/<int:portico_id>', login_required(views.editar_portico), name="editar_portico"),

    # borrar un portico
    path('borrar_portico/<int:portico_id>', login_required(views.borrar_portico), name="borrar_portico"),

    # llamando a la clases 
    path('add_portico', views.PorticoCreate.as_view(), name="add_portico"),

    path('list_portico/', views.PorticoList.as_view(), name='list_portico'),

    path('edit_portico/<int:pk>', views.PorticoUpdate.as_view(), name='edit_portico'),

        path('del_portico/<int:pk>', views.PorticoDelete.as_view(), name='del_portico'),
]
