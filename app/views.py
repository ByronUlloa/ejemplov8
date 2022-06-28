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







 

