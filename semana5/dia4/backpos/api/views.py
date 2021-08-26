from rest_framework.views import APIView
from rest_framework.response import Response
# importar modelos
from .models import Categoria, Mesa, Plato
# importar serializers
from .serializers import CategoriaSerializer, MesaSerializer, CategoriaPlatosSerializer, PedidoPlatosSerializerPOST


# para cambiar la presentación del API
class Response(Response):
    def __init__(self, data=None, message=None, data_status=None, status=None,
                template_name=None, headers=None,
                exception=False, content_type=None):
        
        data_content = {
            'ok': True,
            'content': data
        }
        super(Response, self).__init__(
            data=data_content,
            status=status,
            template_name=template_name,
            headers=headers,
            exception=exception,
            content_type=content_type
        )


class IndexView(APIView):
    
    def get(self, request):
        context = {"ok":True,"message":"El servidor está activo!"}
        return Response(context)
    
    
class CategoriaApiView(APIView):    
    def get(self,request):
        dataCategoria = Categoria.objects.all()
        serializer = CategoriaSerializer(dataCategoria,many=True)
        return Response(serializer.data)
    
    
class MesaApiView(APIView):
    def get(self,request):
        dataMesa = Mesa.objects.all()
        serializer = MesaSerializer(dataMesa,many=True)
        return Response(serializer.data)
    

class CategoriaPlatosApiView(APIView):
    def get(self,request,categoria_id):
        dataCategoria = Categoria.objects.get(categoria_id=categoria_id)
        serializer = CategoriaPlatosSerializer(dataCategoria)
        return Response(serializer.data)


class PedidoApiView(APIView):
    def post(self,request):
        serializer = PedidoPlatosSerializerPOST(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)