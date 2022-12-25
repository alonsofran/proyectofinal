from django.contrib import admin
from .models import Producto, Ofertas, Sucursales

# Register your models here.

admin.site.register(Producto)
admin.site.register(Ofertas)
admin.site.register(Sucursales)
