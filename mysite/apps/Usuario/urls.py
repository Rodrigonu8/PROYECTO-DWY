from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registrar_usuario"),
    path('listar', UserList.as_view(), name="listar_usuario"),
    path('login/', auth_views.LoginView.as_view(template_name='Usuario/login.html'), name='login'),
]
