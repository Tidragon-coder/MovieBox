from django.urls import path

from . import views

urlpatterns = [
    # film liste
    path('', views.film_list, name='film_list'),
    #  ajouter film
    path("addMovie/", views.add_movie, name="addMovie"),
    # Modif film
    path("/<int:pk>/modifier", views.update_movie, name="update_movie"),
]