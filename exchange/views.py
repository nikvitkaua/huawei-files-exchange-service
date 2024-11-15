from django.shortcuts import render
from django.views import generic


# Create your views here.
class IndexView(generic.View):
    template_name = 'exchange/index.html'
