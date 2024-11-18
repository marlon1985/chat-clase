from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('mensajes/',view=views.get_messages,name="get-messages"),
    path('mensajes/create/',view=views.create_messages,name="create-messages"),
]