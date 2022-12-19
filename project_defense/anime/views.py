from django.shortcuts import render

def anime_page(request):
    return render(request, 'common/anime.html')


def anime_details(request):
    return render(request, 'anime/anime_details.html')


def anime_edit(request):
    return render(request, 'anime/anime_edit.html')


def anime_delete(request):
    return render(request, 'anime/anime_delete.html')


def anime_create(request):
    return render(request, 'anime/anime_create.html')

