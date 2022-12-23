from django.shortcuts import render
from .models import Producto


# Create your views here.

def producto(request):
    producto1=Producto(nombre="Huevo de pascua", marca="Kinder", precio=250.20)
    producto1.save()
    return render(request, "templatepadre.html", {"producto":producto1})

def inicio(request):
    return render(request, "AppProyecto/inicio.html", {})

def productoformulario(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        marca=request.POST["marca"]
        precio=request.POST["precio"]
        producto=Producto(nombre=nombre, marca=marca, precio=precio)
        producto.save()
        return render(request, "AppProyecto/productoformulario.html",{})

    else:
        return render(request, "AppProyecto/productoformulario.html")


