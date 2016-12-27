# coding=UTF-8
from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from utilita.util import unique_slugify
import datetime
from django.contrib.auth.models import User
from utilita.thumbs import ImageWithThumbsField


#class Empresa(models.Model):
#
#
#    PENDIENTE = 1
#    ACTIVA = 2
#    NEGADA = 3
#    
#    _STATUS = (
#        (PENDIENTE, _('PENDIENTE')),
#        (ACTIVA, _('ACTIVA')),
#        (NEGADA, _('NEGADA')),
#    )
#
#    EMPRESA = 1
#    PERSONA = 2
#
#    TIPO_EMPRESA = (
#        (EMPRESA, _('EMPRESA')),
#        (PERSONA, _('PERSONA')),
#    )
#
#    nombre = models.CharField(max_length=255)
#    telefono = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'tel\xe9fono')
#    celular = models.CharField(max_length=30, blank=True, null=True)
#    tipo = models.IntegerField(choices=TIPO_EMPRESA, default=1)
#    documento = models.CharField(max_length=255, blank=True, null=True)
#    mail = models.EmailField(blank=False, unique=True) 
#    domicilio = models.CharField(max_length=255)
#    slug = models.SlugField(editable=False)
#    descripcion = models.TextField(blank=True, null=True, verbose_name=u'descripci\xf3n')
#    status = models.IntegerField(choices=_STATUS, default=1)
#    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha de creaci\xf3n')
#    fecha = models.DateTimeField(blank=True, null=True)
#    user = models.ForeignKey(User)
#    logo = ImageWithThumbsField(upload_to='images/logos', 
#                                sizes=((80,80),(50,50),(125,125),(200,200)),
#                                blank=True, null=True)
#    web = models.URLField(_('Web URL'), verify_exists=True, blank=True, null=True)
#       
#    def __unicode__(self):
#        return self.nombre
#
#    @models.permalink
#    def get_absolute_url(self):
#        return ("empresa", [self.slug])
#    
#    def save(self, *args, **kwargs):
#
#        queryset = self.__class__.objects.all()
#        if self.id:
#            queryset = queryset.exclude(id=self.id)
#        self.slug = unique_slugify(self.nombre, queryset, 'slug')
#        super(self.__class__, self).save(*args, **kwargs)
#        

            
        
class Servicio(models.Model):
    

    PENDIENTE = 1
    ACTIVA = 2
    NEGADA = 3
    
    _STATUS = (
        (PENDIENTE, _('PENDIENTE')),
        (ACTIVA, _('ACTIVA')),
        (NEGADA, _('NEGADA')),
    )

    TIPO_PATROCINADO = 0
    TIPO_NORMAL = 1

    TIPO = (
        (TIPO_PATROCINADO, _('PATROCINADO')),
        (TIPO_NORMAL, _('NORMAL')),
    )

    
    nombre = models.CharField(max_length=255)
    #empresa = models.ForeignKey(Empresa)
    descripcion = models.TextField()
    status = models.IntegerField(choices=_STATUS, default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(editable=False)
    tags = models.TextField()
    tipo = models.IntegerField(choices=TIPO, default=1)
    user = models.ForeignKey(User)
    
    
    def __unicode__(self):
        return self.nombre
    
    @models.permalink
    def get_absolute_url(self):
        return ("empresa-servicio-detalle", [self.empresa.slug,
                                      self.slug])      
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(EmpresaServicio, self).save(*args, **kwargs)          