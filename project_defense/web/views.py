from django.shortcuts import render


def index_page(request):
    return render(request, 'common/index.html')


def about_page(request):
    return render(request, 'common/about.html')


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


def photo_details(request):
    return render(request, 'photo/photo_details.html')


def error_404(request):
    return render(request, '404.html')
