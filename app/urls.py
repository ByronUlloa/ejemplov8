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


from django.db import router
from django.urls import path, include
from .views import listar_productos, productos, carrito, ProductoViewset, agregar_productos, modificar_productos, eliminar_productos, listar_productos

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)

urlpatterns = [
    path('', productos, name="productos"),
    path('carrito/', carrito, name="carrito"),
    path('api/', include(router.urls)),
    path('agregar-producto/', agregar_productos, name="agregar_producto"),
    path('modificar-producto/<id>/', modificar_productos, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_productos, name="eliminar_producto"),
    path('listar-producto', listar_productos, name="listar_producto"),
    #path('', base, name="base"),
]
