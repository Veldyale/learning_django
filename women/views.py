from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('<h1>This is home page</h1>')


def index(request):
    return HttpResponse('<h1>This is page women.</h1>')

def categories(request, catid):
    return HttpResponse(f'<h1>Articles ordered by categories</h1> </br><p>{catid}</p>')
