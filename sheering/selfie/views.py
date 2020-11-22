from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Now I am back and none, nothing can stop me.')