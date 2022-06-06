from django.shortcuts import render
from django.http import HttpResponse
 
# Create your views here.



def signup(request):
    return HttpResponse('<h3> Signup Here </h3>')

def login(request):
    return HttpResponse('<h3> login Here </h3>')


def logout(request):
    return HttpResponse('<h3> logout Here </h3>')