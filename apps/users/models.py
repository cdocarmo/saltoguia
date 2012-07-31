# coding=UTF-8
from django.db import models
from django.utils.translation import ugettext as _

import datetime
from django.contrib.auth.models import User



class UserProfile(User):

    date = models.DateTimeField(default=datetime.datetime.now)
    birthday = models.DateField(null=True, blank=True)    
    location = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    validation = models.BooleanField()
    
    
    def __unicode__(self):
        return _("%s %s") % (self.first_name, self.last_name)

    
    def save(self, *args, **kwargs):
        pass
        

