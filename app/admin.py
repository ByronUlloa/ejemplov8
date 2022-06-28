from django.contrib import admin
from .models import Persona

# Register your models here.
class admPersona(admin.ModelAdmin):
    list_display=["rut","nombre","apellido","edad"]
    list_editable=["nombre","apellido","edad"]
    list_filter=["apellido","edad"]
    
    class Meta:
        model=Persona

admin.site.register(Persona,admPersona)
