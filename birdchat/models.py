from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre=models.CharField(max_length=200,unique=True)
    profile_picture=models.ImageField(upload_to="profile_pictures/",blank=True,null=True)
    
    
class Message(models.Model):
   autor=models.ForeignKey(Autor,on_delete= models.CASCADE)
   content=models.TextField()
   creado_en=models.DateTimeField(auto_now_add=True)
