from django.db import models

# Create your models here.
class Pregunta(models.Model):
    # pk ya sale por defecto en todas las tablas
    pregunta_texto = models.CharField(max_length=200)
    fecha_pub = models.DateTimeField(auto_now_add=True)
    
class Opcion(models.Model):
    # fk
    pregunta = models.ForeignKey(Pregunta, on_delete = models.RESTRICT)
    opcion_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default = 0)