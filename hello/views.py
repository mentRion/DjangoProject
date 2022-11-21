from django.shortcuts import render
from django.http import  HttpResponse
from django.views.generic import TemplateView


# Create your views here.

def hello(request):
    return HttpResponse('<html>'
                        '<head>'
                        '<style>'
                        'body{background-color:black;}'
                        'h1{color:white;}'
                        '</style>'
                        '</head>'
                        '<body>'
                        '<h1>Hello, World</h1>'
                        '</body>'
                        '</html>')

class main(TemplateView):
    template_name = 'main.html'