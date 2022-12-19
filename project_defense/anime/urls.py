from django.urls import path, include

from project_defense.anime.views import anime_page, anime_details, anime_create, anime_edit, anime_delete

urlpatterns = (
    path('anime/', anime_page, name='anime page'),
    path('anime/', include(
        [
            path('details/', anime_details, name='anime details page'),
            path('create/', anime_create, name='anime create page'),
            path('edit/', anime_edit, name='anime edit page'),
            path('delete/', anime_delete, name='anime delete page'),
        ]
    ))
)
