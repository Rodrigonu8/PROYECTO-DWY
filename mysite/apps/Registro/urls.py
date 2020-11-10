from django.urls import path, include
from . import views

urlpatterns = [

    # listar las carreras de la bd
    path('listarPorticos', views.listar_porticos, name="listar_porticos"),
]
