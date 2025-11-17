from django.shortcuts import render

# Create your views here.

def index(request): 
    return render(request, "index.html")

def menu(request):
    return render(request, "menu.html")

def sucursales(request):
    return render(request, "sucursales.html")

def contacto(request):
    return render(request, "contacto.html")

def opiniones(request):
    return render(request, "opiniones.html")