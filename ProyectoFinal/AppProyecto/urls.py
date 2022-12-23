from django.urls import path
from AppProyecto.views import *

urlpatterns = [path('producto/', producto),
path('inicio/', inicio),
path('productoformulario/', productoformulario, name='productoformulario'),


]