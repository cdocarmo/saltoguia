from django.db import models

class Searchs(models.Model):
    
    search_word = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.search_word
