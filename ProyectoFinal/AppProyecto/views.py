from django.shortcuts import render
from .models import Producto, Ofertas, Sucursales




# Create your views here.

def producto(request):
    producto1=Producto(nombre="Huevo de pascua", marca="Kinder", precio=250.20)
    producto1.save()
    return render(request, "templatepadre.html", {"producto":producto1})

def inicio(request):
    return render(request, "AppProyecto/inicio.html", {})


def ofertasformulario(request):
    if request.method=="POST":
        oproducto=request.POST["oproducto"]
        onombre=request.POST["onombre"]
        omarca=request.POST["omarca"]
        oprecio_oferta=request.POST["oprecio_oferta"]
        oferta1=Ofertas(oproducto=oproducto, onombre=onombre, omarca=omarca, oprecio_oferta=oprecio_oferta)
        oferta1.save()
        return render(request, 'AppProyecto/inicio.html', {"mensaje":"oferta guardada"})
    else:
        return render(request, "AppProyecto/ofertasformulario.html")
    

def productosformulario(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        marca=request.POST["marca"]
        precio=request.POST["precio"]
        producto=Producto(nombre=nombre, marca=marca, precio=precio)
        producto.save()
        return render(request, 'AppProyecto/inicio.html', {"mensaje":"producto guardado"})
    else:
        return render(request, "AppProyecto/productoformulario.html")

def sucursalesformulario(request):
    if request.method=="POST":
        pais=request.POST["pais"]
        ciudad=request.POST["ciudad"]
        direccion=request.POST["direccion"]
        altura=request.POST["altura"]
        sucursal=Sucursales(pais=pais, ciudad=ciudad, direccion=direccion, altura=altura)
        sucursal.save()
        return render(request, 'AppProyecto/inicio.html', {"mensaje":"sucursal guardada"})
    else:
        return render(request, "AppProyecto/sucursalesformulario.html")

def productobuscar(request):
    return render(request, 'AppProyecto/productobuscar.html')

def buscarp(request):
    nombre=request.GET["nombre"]
    if nombre!="":
        productos= Producto.objects.filter(nombre=nombre)
        return render(request, 'AppProyecto/resultadosbusqueda.html', {"productos": productos})
    else:
        return render(request, 'AppProyecto/productobuscar.html', {"mensaje":"no ingresaste ningun producto"})
