from django.urls import path, include
from rest_framework import routers
from . import views
# from .views import SerieViewSet

# creo ruta nueva
router = routers.DefaultRouter()
# registro mi ruta, nombre(seriesapi) y ruta(SerieViewSet)
router.register(r'seriesapi', views.SerieViewSet)
router.register(r'categoriasapi', views.CategoriaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('seriesall/',SerieViewSet.as_view())
]
