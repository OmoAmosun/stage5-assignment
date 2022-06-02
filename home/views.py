from django.shortcuts import render

# Create your views here.
from http.client import HTTPResponse


from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Home Page </h1>')

def about(request):
    return HttpResponse('<h2> About Page </h2>')

def contact(request):
    return HttpResponse('<h3> Contact Us </h3>')