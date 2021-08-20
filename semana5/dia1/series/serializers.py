from rest_framework import serializers

from .models import Serie, Categoria

# para q me construya los APIs
class SerieSerializer(serializers.HyperlinkedModelSerializer):
    # define la estructura que devuelve
    class Meta:
        model = Serie
        fields = ('id','nombre','categoria')
        
        
class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    # define la estructura que devuelve
    class Meta:
        model = Categoria
        fields = ('id','nombre')
        


    