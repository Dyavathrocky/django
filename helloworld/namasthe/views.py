from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def namaste(request):
    return HttpResponse('this is means hello in hindhi')
