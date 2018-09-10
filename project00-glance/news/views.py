from django.shortcuts import render

# Create your views here.
from .models import Article

def year_archive(request, year):
    article_list = Article.objects.filter(pub_date__year=year)
    context = {
        "article_list" : article_list,
        "year" : year
    }
    return render(request, "news/year_archive.html", context)