from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

from django.contrib.auth.decorators import login_required

import json

# Create your views here.

@login_required(login_url='/admin/login')
def listbooks_view(request):
    listbooks = Book.objects.all()
    #return HttpResponse('OK')
    return render(request, 'books/listbook.html', {'listbooks': listbooks})

def books_view(request, author):
    book = Book.objects.get(author__first_name=author)
    
    data = {
        'title': book.title,
        'order': book.order,
        'cover_image': " %s " % book.cover_image,
        'author': "%s %s" % (book.author.first_name, book.author.last_name),
        'editorial': {
            'name': book.editorial.name,
            'logo': " %s " % book.editorial.logo,
        }
    }   

    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')

