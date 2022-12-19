from django.shortcuts import render, redirect

from project_defense.anime.forms import AnimeCreateForm
from project_defense.anime.models import AnimeTorrent


def crud_action(request, form_class, instance, redirect_url, primary_url):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=instance)
    context = {
        'form': form,
    }
    return render(request, primary_url, context)


def anime_page(request):
    try:
        anime = AnimeTorrent.objects.all()
    except AnimeTorrent.DoesNotExist:
        anime = None

    context = {
        'anime': anime,
    }
    return render(request, 'common/anime.html', context)


def anime_details(request, pk):
    curr_anime = AnimeTorrent.objects.get(pk=pk)
    context = {
        'anime': curr_anime,
    }
    return render(request, 'anime/anime_details.html', context)


def anime_edit(request):
    return render(request, 'anime/anime_edit.html')


def anime_delete(request):
    return render(request, 'anime/anime_delete.html')


def anime_create(request):
    return crud_action(request, AnimeCreateForm, AnimeTorrent(uploader=request.user), 'anime page',
                       'anime/anime_create.html')
