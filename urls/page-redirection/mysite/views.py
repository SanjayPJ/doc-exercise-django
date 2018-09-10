from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    return redirect('redirected_page', 23)

def redirected_page(request, num):
    return HttpResponse("You are done!!!, %d" % num)