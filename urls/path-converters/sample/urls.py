from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:num>', views.int_pass, name='int_pass'),
    path('<str:string>', views.str_pass, name='str_pass'),
    path('<slug:slug>', views.slug_pass, name='slug_pass'),
]