from django.db import models

def upload_path(instance, filename):
    return '/'.join(['covers',str(instance.title),filename])

class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
    upload = models.ImageField(blank=True, null=True, upload_to=upload_path)
