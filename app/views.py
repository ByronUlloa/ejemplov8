from django.shortcuts import get_object_or_404, render,redirect
from .forms import CustomUserCreationForm, frmPerfilUsuario
from django.contrib import messages
from .models import Persona, PerfilUsuario
from django.http import Http404
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .serializers import PersonaSerializer
# Create your views here.


class PersonaViewset(viewsets.ModelViewSet):
        queryset = Persona.objects.all()
        serializer_class = PersonaSerializer




def Home(request):
    return render(request, 'app/Home.html')

def Nosotros(request):
    return render(request,'app/Nosotros.html')


def Donacion(request):
    return render(request, 'app/Donacion.html')


def Pago(request):
    return render(request, 'app/Pago.html')


def Suscripcion(request):
    return render(request, 'app/Suscripcion.html')


def perfilusuario(request):
    form=frmPerfilUsuario(request.POST or None)
    
    contexto={
        "form":form
    }
    if request.method=="POST":
        form=frmPerfilUsuario(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            perfil=PerfilUsuario()
            perfil.rut=datos.get("rut")
            perfil.nombre=datos.get("nombre")
            perfil.apellido=datos.get("apellido")
            perfil.direccion=datos.get("direccion")
            perfil.nombre_usuario=request.user.username
            perfil.save()
            
            
            
            return redirect(to="home")
    
    
    return render(request,"registration/perfilusuario.html",contexto)


def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te Has Registrado Exitosamente")
            return redirect(to="Home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)


def cambiarpassword(request):
    return render(request, 'registration/cambiarpassword.html')


def personas(request):
    datos=[]
    datos=Persona.objects.all()
    total=len(datos)
    
    contexto={
        "personas":datos,
        "totalpersonas":total
    }
    
    return render(request,"app/personas.html",contexto)







 


from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from .models import Producto
from rest_framework import viewsets
from .serializers import ProductoSerializers
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializers

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/productos.html', data)

def carrito(request):
    return render(request, 'app/carrito.html')
    
@permission_required('app.view_producto')
def listar_productos(request):

    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'app/producto/listar.html', data)

@permission_required('app.add_producto')
def agregar_productos(request):

    data = {
        'form': ProductoForm()
    }

    if request.method =='POST':
        formulario=ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)

@permission_required('app.change_producto')
def modificar_productos(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
            data["form"] = formulario

    return render(request, 'app/producto/modificar.html', data)

@permission_required('app.delete_producto')
def eliminar_productos(request, id):
    producto = get_object_or_404(Producto, id=id)

    producto.delete()

    return redirect(to="listar_producto")






