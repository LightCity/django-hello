from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fuck_view_func(req):
    print(req)
    return HttpResponse("Hello, world!")
