from django.db import models
from django import forms
import os
from pr2 import settings

# Create your models here.
class Flupld(models.Model):
    file = models.FileField()
    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.docfile.name))
        super(Flupld,self).delete(*args,**kwargs)