from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','order','book_file','author','editorial')
    list_filter = ('author','editorial')
    ordering = ('order',)

admin.site.register(Book, BookAdmin)
