from django.shortcuts import render, redirect
from . import models
from .models import Opinion
from .forms import OpinionForm
from .models import Producto
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
    return render(request, "sucursales.html")

def contacto(request):
    return render(request, "contacto.html")

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
