from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse('Eat no meat for the whole month')


def february(request):
    return HttpResponse('Go for a run every day')
