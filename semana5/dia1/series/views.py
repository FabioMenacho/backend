# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Serie

from rest_framework import viewsets
from .serializers import SerieSerializer, CategoriaSerializer
from .models import Serie, Categoria

# Create your views here.

# crea metodo get y post
class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# def getall(request):
#     series = Serie.objects.all()
#     data = []
#     for s in series:
#         data.append({
#             'nombre':s.nombre,
#             'categoria':s.categoria,
#             'rating':s.rating
#         })
#     print(data)
#     # pasamos mediante el metodo Json
#     return JsonResponse(data, safe=False)