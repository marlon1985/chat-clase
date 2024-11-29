from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('mensajes/',view=views.get_messages,name="get-messages"),
    path('mensajes/create/',view=views.create_messages,name="create-messages"),
    path("authors/<int:author_id>/",views.update_profile_picture,name="update_profile_picture"),
    path("authors/<str:username>/",views.get_author_by_username,name="get_author_by_username")
]