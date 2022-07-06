from django.shortcuts import render
from django.http import HttpResponse

def HomePageView(HttpResponse):
    return HttpResponse('Hello mf!')

# Create your views here.
