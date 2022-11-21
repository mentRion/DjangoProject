from urllib import request

from django.urls import path
from django.views.generic import TemplateView

from hello import views

urlpatterns = [
    path('',views.hello, name='hello'),
    path('main',TemplateView.as_view(template_name='main.html'),name='main')
]