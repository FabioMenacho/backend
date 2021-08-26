# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Empleado, Cargo
from .serializers import CargoSerializer, EmpleadoSerializer

# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({"message": "Hello, world!"})

@api_view()
def empleados(request):
    dataEmpleado = Empleado.objects.all()
    print(dataEmpleado)
    # data = []
    # for d in dataEmpleado:
    #     data.append({
    #         'nombre':d.nombre,
    #         'email':d.email,
    #         'cargo':d.cargo
    #     })
    # return Response(data)
    serializer = EmpleadoSerializer(dataEmpleado,many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def crearEmpleado(request):
    # nombre = request.data['nombre']
    # email = request.data['email']
    # cargo = request.data['cargo']
    # nuevoEmpleado = Empleado.objects.create(nombre=nombre,email=email,cargo=cargo)
    # data={
    #     'respuesta':'OK'
    # }
    # return Response(data)
    
    # print("request.data")
    # print(request.data)
    serializer = EmpleadoSerializer(data=request.data)
    # print("serializer")
    # print(serializer)
    serializer.is_valid(raise_exception=True)
    nuevoEmpleado = serializer.save()
    # data = serializer.data
    # print("data")
    # print(data)
    # lo de abajo se ha reescrito en el archivo serializer
    # nuevoEmpleado = Empleado.objects.create(**data)    
    
    return Response(EmpleadoSerializer(nuevoEmpleado).data)

@api_view(['GET','POST'])
def cargos(request):
    if request.method == 'GET':
        dataCargos = Cargo.objects.all()
        serializer = CargoSerializer(dataCargos,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CargoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
