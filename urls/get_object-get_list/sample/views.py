from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Test
from django.http import HttpResponse

# Create your views here.

def get_object(request, num):
    obj = get_object_or_404(Test, pk=num)
    return HttpResponse(obj)

def get_objects(request):
    objs = get_list_or_404(Test, true_tab=True)
    return HttpResponse(objs)