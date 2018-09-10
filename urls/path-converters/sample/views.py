from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome Home!")

def int_pass(request, num):
    return HttpResponse("%d" % num)

def str_pass(request, string):
    return HttpResponse('%s' % string)

def slug_pass(request, slug):
    return HttpResponse("%s" % slug)