from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import RESTRICT
from django.db.models.fields import DecimalField, IntegerField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('fecha registro')
    imagen = models.ImageField(upload_to='productos', blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.RESTRICT)
    doc_ide =  models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return str(self.pk)
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    fecha = models.DateField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.pk)
    
class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=RESTRICT)
    producto = models.ForeignKey(Producto, on_delete=RESTRICT)
    cantidad = IntegerField(default=1)
    subtotal = DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.producto.nombre
    