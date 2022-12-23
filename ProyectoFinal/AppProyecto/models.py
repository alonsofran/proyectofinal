from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.marca +""+ self.nombre

class Sucursales(models.Model):
    pais=models.CharField(max_length=60)
    ciudad=models.CharField(max_length=60)
    direccion=models.CharField(max_length=60)
    altura=models.IntegerField()

    def __str__(self):
        return self.pais +" "+ self.ciudad +" "+ self.direccion + " " + self.altura

class Ofertas(models.Model):
    oproducto=models.CharField(max_length=50)
    onombre=models.CharField(max_length=50)
    omarca=models.CharField(max_length=50)
    oprecio_oferta=models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.oproducto + " " + self.onombre
