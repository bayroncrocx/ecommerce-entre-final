from django.db import models

# Create your models here.

class Reporteria(models.Model):
    # id_repor = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, blank=True)
    product_name = models.CharField(max_length=50, blank=True)
    slug = models.CharField(max_length=50, blank=True)
    accion = models.CharField(max_length=50, blank = True)
    create_date = models.DateField(auto_now_add =True)
    hora = models.TimeField(auto_now_add =True )
    stock  = models.IntegerField()


class Inventario(models.Model):
    id_producto = models.CharField(max_length=50, blank=True)
    product_name = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, blank=True)
    slug = models.CharField(max_length=50, blank=True)
    stock_inicial = models.CharField(max_length=50, blank=True)
    entradas = models.CharField(max_length=50, blank=True)
    #salidas = models.CharField(max_length=50, blank=True)
    #total = models.CharField(max_length=50, blank=True)
    price = models.IntegerField()
    total_price = models.IntegerField()
    create_date = models.DateField(auto_now_add =True)


