from django.db import models
from django.contrib.auth.models import User


class Telefono(models.Model):
    tipo = (
        ('TEL', 'Telefono'),
        ('CEL', 'Celular'),
    )
    
    tipo = models.CharField(max_length=3, choices=tipo)
    usuario = models.ForeignKey(User)
    
    
class Area(models.Model):
    tipo = (
        ('EMPRESARIAL', 'Empresarial',),
        ('PROFESIONAL', 'Profesional',),
        ('OFICIO', 'Oficio',),
        ('MERCANTIL', 'Mercantil',),
    )
    
    nombre = models.CharField(max_length=11, choices=tipo)
    
    
class Rubro(models.Model):
    nombre = models.CharField(max_length=30)
    area = models.ManyToManyField(Area)
    

class SubRubro(models.Model):
    nombre = models.CharField(max_length=30)
    rubro = models.ForeignKey(Rubro)
    
    
class Servicio(models.Model): 
    descripcion = models.TextField()
    telefono = models.CharField(max_length=16, null=True, blank=True)
    usuario = models.ForeignKey(User)
    subrubro = models.ForeignKey(SubRubro, null=True)
    

User.add_to_class('categoria', models.ForeignKey(Area, null=True))
User.add_to_class('nombre_marca', models.CharField(max_length=60))
User.add_to_class('avatar', models.ImageField(upload_to='avatares'))  # imagen perfil
User.add_to_class('domicilio', models.CharField(max_length=80))  # domicilio
User.add_to_class('horarios', models.CharField(max_length=180))  # horarios
User.add_to_class('dias_habiles', models.CharField(max_length=180))  # dias habiles
User.add_to_class('aclaraciones', models.CharField(max_length=220))  # aclaraciones

