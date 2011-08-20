# coding=UTF-8
from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify

import datetime
from django.contrib.auth.models import User



class Empresa(models.Model):

    PENDIENTE = 1
    ACTIVA = 2
    NEGADA = 3

    STATUS_EMPRESA = (
        (PENDIENTE, _('PENDIENTE')),
        (ACTIVA, _('ACTIVA')),
        (NEGADA, _('NEGADA')),
    )

    EMPRESA = 1
    PERSONA = 2

    TIPO_EMPRESA = (
        (EMPRESA, _('EMPRESA')),
        (PERSONA, _('PERSONA')),
    )

    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=30)
    celular = models.CharField(max_length=30)
    tipo = models.IntegerField(choices=TIPO_EMPRESA, default=1)
    documento = models.CharField(max_length=255)
    mail = models.EmailField(blank=False, unique=True) 
    domicilio = models.CharField(max_length=255)
    slug = models.SlugField(editable=False)
    descipcion = models.TextField()
    status = models.IntegerField(choices=STATUS_EMPRESA, default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Empresa, self).save(*args, **kwargs)
        
        