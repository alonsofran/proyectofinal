from django.urls import path
from AppProyecto.views import *

urlpatterns = [
path('producto/', producto, name='producto'),
path('', inicio, name='inicio'),
path('ofertasformulario/', ofertasformulario, name='ofertasformulario'),
path('productosformulario/', productosformulario, name='productosformulario'),
path('sucursalesformulario/', sucursalesformulario, name='sucursalesformulario'),
path('productobuscar/', productobuscar, name='productobuscar'),
path('buscarp/', buscarp, name='buscarp'),
]