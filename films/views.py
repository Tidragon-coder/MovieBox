from django.shortcuts import render
from django.http import HttpResponse
from .models import Film

def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films})

def test(request):
    return render(request, 'films/film_add.html')

# Create your views here.