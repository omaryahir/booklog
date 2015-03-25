from django.db import models

# Create your models here.

class Editorial(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='files/editorial',blank=True,null=True)

    def __unicode__(self):
        return self.name
