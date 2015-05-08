# -*- coding: utf8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Book
from django.contrib.auth.decorators import login_required
import json
from django.core import serializers
from .forms import SumaForm, BookForm, ContactForm
from .models import Book

from django.views.generic import TemplateView, FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .mixins import LoginRequiredMixin


# Create your views here.

@login_required(login_url='/admin/login')
def listbooks_view(request):
    listbooks = Book.objects.all()
    #return HttpResponse('OK')
    return render(request, 'books/listbook.html', {'listbooks': listbooks})

def books_view(request, author):
    book = get_object_or_404(Book, author__first_name=author)
    
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


def books_serial_view(request):
    data = serializers.serialize("json", Book.objects.all())
    return HttpResponse(data, content_type='application/json')

def suma_view(request):
    
    resultado = 0
    if request.method == "POST":
        form = SumaForm(request.POST) 
        if form.is_valid():
            valor1 = form.cleaned_data['valor1']
            valor2 = form.cleaned_data['valor2']
            valor3 = form.cleaned_data['valor3']

            resultado = float(valor1) + float(valor2)
    else:
        form = SumaForm()

    return render(request, 'books/suma.html', {"form":form, "resultado":resultado})

def book_create_view(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect("/listbooks/")
    else:
        form = BookForm()
    return render(request, 'books/form.html', {"form":form}) 

def book_edit_view(request, id_book):
    b = Book.objects.get(pk=id_book)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=b)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/listbooks/")
    else:
        form = BookForm(instance=b)

    return render(request, 'books/form.html', {'form':form})


class csrfExceptMixin(object):
    """docstring for csrfExceptMixin"""
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print "csrfExceptMixin"
        return super(csrfExceptMixin, self).dispatch(request, *args, **kwargs)


class MyMostBasicView(csrfExceptMixin, LoginRequiredMixin, TemplateView):
    """docstring for MyMostBasicView"""
    template_name = "template_base.html"
   
    #@method_decorator(csrf_exempt)
    #def dispatch(self, request, *args, **kwargs):
    #    print "MyMostBasicView"
    #    return super(MyMostBasicView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MyMostBasicView, self).get_context_data(**kwargs)
        context["saludo"] = "Hola Mundo !"
        return context
 
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['mensaje'] = "Método GET"
        ret = dict(context)
        del ret['view']
        print type(ret), ret
        return HttpResponse(json.dumps(ret))

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['mensaje'] = "Método GET"
        ret = dict(context)
        del ret['view']
        print type(ret), ret
        return HttpResponse(json.dumps(ret))

       

class CreateSessionView(TemplateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CreateSessionView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        my_session = {}
        if 'key' in request.GET:
            value = request.session.get(request.GET['key'], None)
            if value is not None:
                my_session[request.GET['key']] = request.session[request.GET['key']]
            else:
                my_session['msg'] = u"La variable %s no existe en sesión." % request.GET['key']
        else:
            my_session.update({'msg': "Error. Solicitud mal formada"})
        return HttpResponse(json.dumps(my_session))

    def post(self, request, *args, **kwargs):
        my_session = {}
        if 'add' in request.POST:
            if 'key' in request.POST and 'value' in request.POST:
                request.session[request.POST['key']] = request.POST['value']
                my_session['msg'] = u"La variable de sesión %s ha sido registrada correctamente" % request.POST['key']
        elif 'delete' in request.POST and 'key' in request.POST:
            if request.session.get(request.POST['key'], None) is not None:
                del request.session[request.POST['key']]
                my_session['msg'] = u"La variable de sesión %s ha sido eliminada correctamente" % request.POST['key']
        else:
            my_session.update({'msg': "Error. Solicitud mal formada"})
        return HttpResponse(json.dumps(my_session))


class ContactView(FormView):
    """
    Class-based View for the contact page ...
    """
    template_name = "contact.html"
    form_class = ContactForm
    success_url = '/contact/thank_you'

    def form_valid(self, form):
        form.send_mail()
        return super(ContactView, self).form_valid(form)


class TemplateTestView(TemplateView):
    template_name = "template_tag.html"
    """ docstring for TemplateTestView """
    def get_context_data(self, **kwargs):
        context = super(TemplateTestView, self).get_context_data(**kwargs)
        context["table"] = {
            'title': ["#", "Nombre", "Apellidos"],
            'content':
            [
                [1, "Anacleto", "Gómez"],
                [2, "José", "López"],
                [3, "Maria", "Gónzalez"],
            ]
        }
        return context


class FilterTestView(TemplateView):
    template_name = "template_filter.html"
    
    def get_context_data(self, **kwargs):
        context = super(FilterTestView, self).get_context_data(**kwargs)
        context['my_string'] = "Pero abajo del sombrero ..."
        return context

