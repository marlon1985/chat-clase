from rest_framework import serializers
from .models import Autor,Message

class AutorSerializer(serializers.ModelSerializer) :
      class Meta:
            model=Autor
            fields="__all__"


class MensajeSerializer(serializers.ModelSerializer):
      class Meta:
            model=Message
            fields="__all__"     