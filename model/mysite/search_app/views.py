from django.shortcuts import render
from .models import Person

# Create your views here.


def index(request):
    return render(request, 'search_app/index.html')


def search(request):
    if request.method == 'POST':
        name = request.POST['name']
        persons = Person.objects.filter(name__contains=name)
        return render(request, 'search_app/search_result.html', {
            'search_text': name,
            'persons': persons,
        })
