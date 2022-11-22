import contextlib
from msilib.schema import ListView
from tkinter import N
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout, login

from django.http import HttpResponse

from .models import Moto
from .forms import MotoForm

from django.db.models import Q



# Create your views here.


@login_required
def logout_view(request):
    logout(request)
    return redirect('inicio')

def salir(request):
    logout(request)
    return redirect('')

def index(request):
    return render(request, 'motos/inicio.html',)




def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')




def motos(request):
    if request.GET.get('buscar'):
        queryset = request.GET['buscar']
        motos = Moto.objects.filter(
            Q(cliente__icontains = queryset) |  
            Q(patente__icontains = queryset) |
            Q(vehiculo__icontains = queryset)
        )
    else:
        motos = Moto.objects.all()
    context = {
        'motos': motos
    }
    return render(request, 'motos/index.html', context)
  


def crear(request):
    formulario = MotoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('motos')
    return render(request, 'motos/crear.html', {'formulario': formulario})

def editar(request, id):
    moto = Moto.objects.get(id = id)
    formulario = MotoForm(request.POST or None, instance = moto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('motos')
    return render(request, 'motos/editar.html', {'formulario': formulario})

def detalles(request, id):
    moto = Moto.objects.get(id = id)
    formulario = MotoForm(request.POST or None, instance = moto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('motos')
    return render(request, 'motos/detalles.html', {'formulario': formulario})


def eliminar(request, id):
    moto = Moto.objects.get(id = id)
    moto.delete()
    return redirect('motos')


def buscar(request):
    if request.GET['buscar']:
        queryset = request.GET['buscar']
        motos = Moto.objects.filter(
            Q(cliente__icontains = queryset) |  
            Q(patente__icontains = queryset) |
            Q(vehiculo__icontains = queryset)
        ).distinct()
        return render(request, 'motos/busqueda.html', {'motos': motos, 'query': queryset})
    else:
        mensaje = "No ha introducido nada."
    return HttpResponse(mensaje)

