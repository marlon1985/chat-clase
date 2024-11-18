from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre=models.CharField(max_length=150,unique=True)
    
    
class Message(models.Model):
   Autor=models.ForeignKey(Autor,on_delete= models.CASCADE)
   content=models.TextField()
   creado_en=models.DateTimeField(auto_now_add=True)
