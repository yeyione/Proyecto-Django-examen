from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Esta es la vista HOME")

def about(request):
    return HttpResponse("Esta es la vista ABOUT")
