from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    book_file = models.FileField(upload_to='books')

