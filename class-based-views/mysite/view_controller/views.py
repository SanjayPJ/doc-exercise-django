from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class DemoTemplateView(TemplateView):
    template_name = "view_controller/demo.html"