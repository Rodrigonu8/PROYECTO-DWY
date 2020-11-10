from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q 
from .models import Portico, Bicicleta


# Create your views here.
def listar_porticos(request):
    porticos = Portico.objects.all()
    return render(request, "Registro/listar_porticos.html", {'porticos': porticos})

def listar_bicicletas(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, "Registro/listar_bicicletas.html", {'bicicletas': bicicletas}) 