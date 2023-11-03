from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def register(request):
    return HttpResponse('This is registration page!')

def my_login(request):
    return HttpResponse('this is the ligi page')

def home(request):
    return HttpResponse('Home page')