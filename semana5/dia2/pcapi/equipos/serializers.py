from rest_framework import serializers
from .models import Empleado, Cargo

# para armar el formato json de salida, evita el uso de un for para hacer el formato
class EmpleadoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    email = serializers.EmailField()
    cargo = serializers.CharField()
    
    def create(self,validated_data):
        return Empleado.objects.create(**validated_data)
    

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'
    