from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.first_name
