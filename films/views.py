from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Film
from django.db.models import Avg

from .forms import FilmForm

def film_list(request):
    films = Film.objects.all()
    note_moy = round(films.aggregate(moyenne=Avg('note'))['moyenne'], 1)
    return render(request, 'films/film_list.html', {'films': films, 'note_moy': note_moy})

def add_movie(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('film_list')  
    else:
        form = FilmForm()
    
    return render(request, 'films/film_add.html', {'form': form})

def update_movie(request, pk):
    film = Film.objects.get(pk=pk)
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = FilmForm(instance=film)
    
    return render(request, 'films/film_update.html', {'form': form, 'film': film})

# Create your views here.