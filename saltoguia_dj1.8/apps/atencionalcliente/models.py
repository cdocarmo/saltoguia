from django.db import models
from django.contrib.auth.models import User


class MensajeContacto(models.Model):
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    comentarios = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    visto = models.BooleanField(default=False)
    
    
class RespuestaMsnContacto(models.Model):
    duenio = models.ForeignKey(User)
    msn_contacto = models.ForeignKey(MensajeContacto)
    respuesta = models.TextField()
    enviado = models.DateTimeField(auto_now_add=True)
    