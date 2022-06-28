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

from django.contrib import admin
from .models import Marca, Producto
# Register your models here.

admin.site.register(Marca)
admin.site.register(Producto)