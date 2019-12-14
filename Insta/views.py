#from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HelloWord(TemplateView):
    template_name = 'test.html'

