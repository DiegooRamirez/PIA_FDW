from django.shortcuts import render, redirect
from . import models
from .models import Opinion
from .forms import OpinionForm, ContactoForm
from .models import Producto
from .models import Sucursal
from .models import Evento
# Create your views here.

def index(request): 
    ultimos_productos = Producto.objects.order_by('-id')[:3]
    return render(request, "index.html", {"ultimos_productos": ultimos_productos})

def menu(request):
    datos={
        "productos":models.Producto.objects.all()
        }
    return render(request, "menu.html", context=datos)

def sucursales(request):
    sucursales = Sucursal.objects.all()
    eventos = Evento.objects.select_related('sucursal').order_by('fecha', 'hora')
    return render(request, 'sucursales.html', {
        'sucursales': sucursales,
        'eventos': eventos
    })

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto')
    else:
        form = ContactoForm()
    return render(request, "contacto.html", {"form": form})

def opiniones(request):
    opiniones = Opinion.objects.all().order_by('-fecha')

    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opiniones')  # redirige a la misma página
    else:
        form = OpinionForm()

    return render(request, 'opiniones.html', {
        'opiniones': opiniones,
        'form': form
    })
