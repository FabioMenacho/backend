from django.shortcuts import render, redirect
from .models import Producto, Cliente
from django.conf import settings
# lo importamos de nuestro archivo forms las clases ClienteGForm y usuarioForm
from .forms import ClienteForm, UsuarioForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from .carrito import Cart
# Create your views here.

def index(request):
    lista_productos = Producto.objects.all()
    print(settings.MEDIA_URL)
    context = {'lstProductos': lista_productos, 'directorio_img':settings.MEDIA_URL}
    return render(request, 'index.html',context)

def registro(request):
    frmCliente = ClienteForm()
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        frmNuevoCliente = ClienteForm(request.POST)
        # check whether it's valid:
        if frmNuevoCliente.is_valid():
            data = frmNuevoCliente.cleaned_data
            # lo sacamos de forms.py
            dataUsuario = data['usuario']
            dataPassword = data['clave']       
            # creamos usuarios para la tabla auth_user sino no puedo crear la tabla cliente
            nuevoUsuario = User.objects.create_user(username=dataUsuario, password=dataPassword)
            nuevoUsuario.first_name = data['nombres']
            nuevoUsuario.last_name = data['apellidos']
            nuevoUsuario.email = data['email']
            nuevoUsuario.save()
            # creamos datos para la tabla cliente
            nuevoCliente = Cliente(usuario=nuevoUsuario)
            nuevoCliente.telefono = data['telefono']
            nuevoCliente.direccion = data['direccion']
            nuevoCliente.doc_ide = data['doc_ide']
            nuevoCliente.save()
            
            return render(request,'graciasRegistro.html')
    
    context = {
        'frmCliente':frmCliente
    }
    return render(request,'registroCliente.html', context)

def loginUsuario(request):
    frmUsuario = UsuarioForm()
    
    if request.method == 'POST':
        frmLogin = UsuarioForm(request.POST)
        if frmLogin.is_valid():
                data = frmLogin.cleaned_data
                # lo sacamos de forms.py
                dataUsuario = data['usuario']
                dataPassword = data['clave']  
                
                loginUsuario = authenticate(request, username=dataUsuario, password=dataPassword)
                if loginUsuario is not None:
                    # estoy logeando
                    login(request,loginUsuario)
                    return render(request,'cuenta.html')
                else:
                    context = {
                        'form': frmUsuario,
                        'error':'datos erroneos'
                    }
                    return render(request, 'login.html',context)
    
    context = {
        'form': frmUsuario
    }
    return render(request, 'login.html',context)

def producto(request, producto_id):
    # para atrapar 1 objeto producto con el id seleccionado
    objProducto = Producto.objects.get(id=producto_id)
    context = {
        'producto':objProducto,
        'directorio_img':settings.MEDIA_URL
    }
    return render(request, 'producto.html', context)

# para agregar
def agregarCarrito(request,producto_id):
    # obtiene un objeto de compra
    objProducto = Producto.objects.get(id=producto_id)
    # ya tiene todos los productos anteriores seleccionados
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))    
    return render(request,'carrito.html')

def eliminarProductoCarrito(request, producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    return render(request,'carrito.html')

# para ver el carrito
def carrito(request):
    print(request.session.get("cart"))
    return render(request,'carrito.html')