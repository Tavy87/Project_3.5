from django.shortcuts import render
from django.http import HttpResponse
from .models import Widget

def index(request):
    return HttpResponse('<h1>Wacky Widgets</h1>')
