from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Film

from .forms import FilmForm

def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films})

def add_movie(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('film_list')  
    else:
        form = FilmForm()
    
    return render(request, 'films/film_add.html', {'form': form})

# Create your views here.