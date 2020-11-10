from django.shortcuts import render, redirect
from django.db.models import Q 
from .models import Portico, Bicicleta
from .forms import porticoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

#listar porticos y bicicletas
def listar_porticos(request):
    porticos = Portico.objects.all()
    return render(request, "Registro/listar_porticos.html", {'porticos': porticos})

def listar_bicicletas(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, "Registro/listar_bicicletas.html", {'bicicletas': bicicletas})  

 # agregar portico
 
def agregar_portico(request):
    if request.method == "POST":
        form = porticoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_portico")
    else:
        form = porticoForm()
        return render(request, "Registro/agregar_portico.html", {'form': form})


# borrar portico

def borrar_portico(request, portico_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Portico.objects.get(id=portico_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_portico')

# editar porticco


def editar_portico(request, portico_id):
    # Recuperamos la instancia de la carrera
    instancia = Portico.objects.get(id=portico_id)

    # Creamos el formulario con los datos de la instancia
    form = porticoForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = porticoForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "Registro/editar_portico.html", {'form': form})


# clases crear portico

class PorticoCreate(CreateView):
    model = Portico
    form_class = porticoForm
    template_name = 'Registro/agregar_portico.html'
    success_url = reverse_lazy("listar_porticos")

# clase listar portico

class PorticoList(ListView):
    model = Portico
    template_name = 'Registro/listar_porticos.html'

# clase modificar portico
class PorticoUpdate(UpdateView):
    model = Portico
    form_class = porticoForm
    template_name = 'Registro/editar_portico.html'
    success_url = reverse_lazy('listar_porticos')


# clase borrar portico

class PorticoDelete(DeleteView):
    model = Portico
    template_name = 'Registro/portico_delete.html'
    success_url = reverse_lazy('listar_porticos')


 