from django.db import models
from django.utils import timezone

# Create your models here.

# para crear tablas

# tabla padre
class Pregunta(models.Model):
    # pk ya sale por defecto en todas las tablas
    pregunta_texto = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
# tabla hijo
class Opcion(models.Model):
    # fk
    pregunta = models.ForeignKey(Pregunta, on_delete = models.RESTRICT)
    opcion_text = models.CharField(max_length=200)
    votos = models.IntegerField(default = 0)
    