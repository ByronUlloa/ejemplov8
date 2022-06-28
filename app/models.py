from django.db import models


# Create your models here.

class Persona(models.Model):
    rut=models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    
    def __str__(self):
        return  f"{self.rut} - {self.nombre} {self.apellido}"



class PerfilUsuario(models.Model):
    nombre_usuario=models.CharField(primary_key=True,max_length=50)
    rut=models.CharField(unique=True,max_length=10)
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    direccion=models.CharField(max_length=250)
  
    
    def __str__(self):
        return self.nombre + " " + self.apellido



from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre =models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre