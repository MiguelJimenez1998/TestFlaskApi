from rest_framework import serializers
from .models import Adress, House

class AdressSelializer(serializers.ModelSerializer) :
    class Meta:
        model=Adress
        fields='__all__'

class HouseSelializer(serializers.ModelSerializer) :
    class Meta:
        model=House
        fields='__all__'
