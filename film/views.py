from django.shortcuts import render

from film.models import Film, Actor, Genre


def main_view(request):
    return render(request, "main.html")


def films_view(request):
    all_films = Film.objects.all()
    films = [film for film in all_films if film.rating > 8]
    context = {'films': films}
    return render(request, 'films/films.html', context)
