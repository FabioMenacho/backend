from django.shortcuts import render
from .models import Producto
from django.conf import settings

# Create your views here.

def index(request):
    lista_productos = Producto.objects.all()
    print(settings.MEDIA_URL)
    context = {'lstProductos': lista_productos, 'directorio_img':settings.MEDIA_URL}
    return render(request, 'index.html',context)
