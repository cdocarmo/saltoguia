# coding=UTF-8
from utilita.thumbs import ImageWithThumbsField

from django.db import models
from django.utils.translation import ugettext as _

import datetime
from django.contrib.auth.models import User



class UserProfile(User):
    
    
    PENDIENTE = 1
    ACTIVA = 2
    NEGADA = 3
    
    _STATUS = (
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
    
    date = models.DateTimeField(default=datetime.datetime.now)
    birthday = models.DateField(null=True, blank=True)    
    location = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    validation = models.BooleanField()
    
    #nombre = models.CharField(max_length=255) #el nombre es de user: ej name = hygies
    # para que no quede name = Fulanito, name_empresa = hygies (usuario = empresa)
    telefono = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'tel\xe9fono')
    celular = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.IntegerField(choices=TIPO_EMPRESA, default=1)
    documento = models.CharField(max_length=255, blank=True, null=True)
    mail = models.EmailField(blank=False, unique=True) 
    domicilio = models.CharField(max_length=255)
    slug = models.SlugField(editable=False)
    descripcion = models.TextField(blank=True, null=True, verbose_name=u'descripci\xf3n')
    status = models.IntegerField(choices=_STATUS, default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha de creaci\xf3n')
    fecha = models.DateTimeField(blank=True, null=True)
    #user = models.ForeignKey(User)
    logo = ImageWithThumbsField(upload_to='images/logos', 
                                sizes=((80,80),(50,50),(125,125),(200,200)),
                                blank=True, null=True)
    web = models.URLField(_('Web URL'), verify_exists=True, blank=True, null=True)
    
    def __unicode__(self):
        return _("%s %s") % (self.first_name, self.last_name)

    @models.permalink
    def get_absolute_url(self):
        return ("empresa", [self.slug]) #ver como funciona esto
    
    def save(self, *args, **kwargs):

        queryset = self.__class__.objects.all()
        if self.id:
            queryset = queryset.exclude(id=self.id)
        self.slug = unique_slugify(self.nombre, queryset, 'slug')
        super(self.__class__, self).save(*args, **kwargs)
    #def save(self, *args, **kwargs):
    #    pass
        

