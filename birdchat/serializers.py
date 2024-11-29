from rest_framework import serializers
from .models import Autor,Message

class AutorSerializer(serializers.ModelSerializer) :
      profile_picture = serializers.ImageField(allow_empty_file=True, required=False)
      class Meta:
            model=Autor
            fields="__all__"

class MensajeSerializer(serializers.ModelSerializer):
      autor=AutorSerializer(read_only=True) ### la variabledebellamarse igual que en la base de datos"autor"
      class Meta:
            model=Message
            fields="__all__"      
            #fields = ["id", "autor", "content", "creado_en"]