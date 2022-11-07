from django.shortcuts import render
from django.http import  HttpResponse

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
