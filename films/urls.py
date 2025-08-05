from django.urls import path

from . import views

urlpatterns = [
    path('', views.film_list, name='film_list'),
    path("addMovie/", views.add_movie, name="addMovie"),
    path("/<int:pk>/modifier", views.update_movie, name="update_movie"),
]