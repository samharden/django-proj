from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World this is the FL Discrim index page")

def search(request):
    return HttpResponse("Search Page")

# Create your views here.
