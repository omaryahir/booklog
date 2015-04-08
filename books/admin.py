from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','order','cover_image','author','editorial','image_tag')
    list_filter = ('author','editorial')
    ordering = ('order',)
    readonly_fields=('image_tag',)

admin.site.register(Book, BookAdmin)
