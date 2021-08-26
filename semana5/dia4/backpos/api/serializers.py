from rest_framework import serializers
from .models import Categoria, Plato, Mesa, Pedido, PedidoPlatos

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        # fields = '__all__'
        # le quitamos el all para que no aparezcan en el API
        fields = '__all__'
        
    # def to_representation(self,instance):
    #     representation = super().to_representation(instance)
    #     representation['categoria_id'] = instance.pk
    #     representation['categoria_nom'] = instance.nombre
        
        # return representation


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'
        
    # def to_representation(self,instance):
    #     representation = super().to_representation(instance)
    #     representation['mesa_id'] = instance.pk
    #     representation['mesa_nro'] = instance.numero
    #     representation['mesa_cap'] = instance.capacidad
        
        # return representation
    
    
class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'    
    
    # para aumentar el http:/localhost:8000 sino no sale la imagen
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        representation['plato_img'] = 'http://localhost:8000' + instance.plato_img.url
        return representation


class CategoriaPlatosSerializer(serializers.ModelSerializer):
    Platos = PlatoSerializer(many=True,read_only=True)
    class Meta:
        # me trae la categoria seleccionada en views
        model = Categoria
        # trae los platos de esa categoria
        fields = ['categoria_id','categoria_nom','Platos']
        

class PedidoPlatosSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = PedidoPlatos
        fields = ['plato_id','pedidoplato_cant']


class PedidoSerializer(serializers.ModelSerializer):
    pedidoPlatos = PedidoPlatosSerializerPOST(many=True)
    class Meta:
        model = Pedido
        fields = ['pedido_fech','pedido_nro','pedido_est','usu_id','mesa_id','pedidoplatos']
        
    def create(self, validated_data):
        pedidos_data = validated_data.pop('pedidoplatos')
        pedido = Pedido.objects.create(**validated_data)
        for pedido_data in pedidos_data:
            PedidoPlatos.objects.create(pedido_id=pedido, **pedido_data)
        return pedido