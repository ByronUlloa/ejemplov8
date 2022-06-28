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


