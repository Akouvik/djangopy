from django.shortcuts import render
from django.http import HttpResponse

# you create a view using functions


def myView(request):
    return HttpResponse("Hello, world!")
