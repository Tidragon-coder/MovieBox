from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Film
from django.db.models import Avg

from .forms import FilmForm

# afficher la list de films (et la moyenne des notes)
def film_list(request):
    films = Film.objects.all().order_by('-id')
    moyenne = films.aggregate(moyenne=Avg('note'))['moyenne']
    note_moy = round(moyenne, 1) if moyenne is not None else 0
    return render(request, 'films/film_list.html', {'films': films, 'note_moy': note_moy})

# Ajouter un film
def add_movie(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('film_list')  
    else:
        form = FilmForm()
    
    return render(request, 'films/film_add.html', {'form': form})

# Modifier un film
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



