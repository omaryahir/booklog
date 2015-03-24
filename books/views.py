from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def listbooks_view(request):
    listbooks = Book.objects.all()
    #return HttpResponse('OK')
    return render(request, 'listbook.html', {'listbooks': listbooks})
