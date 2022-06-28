from django import forms
from .models import Persona, PerfilUsuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields =['username', "first_name", "last_name", "email", "password1", "password2"]

class frmPerfilUsuario(forms.ModelForm):
    
    class Meta:
        model=PerfilUsuario
        fields=["rut","nombre","apellido","direccion"]


