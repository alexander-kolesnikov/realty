from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello everyone. Here will be index page")

def search(request):
    return HttpResponse("That's the search page")