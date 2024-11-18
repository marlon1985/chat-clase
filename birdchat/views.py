from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AutorSerializer, MensajeSerializer  
from .models import Autor, Message  # Cambiado a PascalCase

@api_view(["GET"])
def get_messages(request):
    messages = Message.objects.all().order_by("creado_en")
    serializer = MensajeSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create_messages(request):
    username = request.data.get("username")
    content = request.data.get("content")
   # Verificación de datos requeridos
    if not username or not content:
        return Response(
            {"error": "Los campos 'username' y 'content' son requeridos."},
            status=status.HTTP_400_BAD_REQUEST
        )    
    # Crea o busca el autor y desestructura la tupla correctamente
    autor, created = Autor.objects.get_or_create(nombre=username)
    # Crear el mensaje usando el serializador
    serializer = MensajeSerializer(data={"content": content, "Autor": autor.id}) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
