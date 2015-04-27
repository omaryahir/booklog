from django.db import models
from editorial.models import Editorial
from authors.models import Author

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='files/books')

    editorial = models.ForeignKey(Editorial)
    author = models.ForeignKey(Author)

    published = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.title

    def image_tag(self):
        if self.cover_image:
            return u'<img src="%s" width=100 />' % self.cover_image.url
        else:
            return u'Sin imagen'
    
    image_tag.short_description = 'Cubierta'
    image_tag.allow_tags = 'True'
