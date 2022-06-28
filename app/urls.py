from django.urls import path, include
from .views import Home, Nosotros, Donacion, Pago, Suscripcion, perfilusuario, registro, cambiarpassword, personas, PersonaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Persona', PersonaViewset)

#localhost:8000/api/persona
urlpatterns = [
    path('', Home , name="Home"),
    path('Nosotros/',Nosotros,name="Nosotros"),
    path('Donacion/',Donacion,name="Donacion"),
    path('Pago/',Pago, name="Pago"),
    path('Suscripcion/',Suscripcion, name="Suscripcion"),
    path('registro/',registro,name="registro"),
    path('personas/',personas,name="personas"),
    path('perfilusuario/',perfilusuario,name="perfilusuario"),
    path('cambiarpassword/',cambiarpassword,name="cambiarpassword"),
    path('api/',include(router.urls)),
]

