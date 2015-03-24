from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def listbooks_view(request):
    return HttpResponse('OK')
