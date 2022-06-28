from pyexpat import model
from .models import Producto
from rest_framework import serializers


class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
        
from dataclasses import fields
from rest_framework import serializers