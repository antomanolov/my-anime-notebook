from django.urls import path, include

from project_defense.web.views import index_page, about_page, anime_page, \
    anime_details, anime_create, anime_edit, anime_delete, photo_details, error_404

urlpatterns = (
    path('', index_page, name='index page'),
    path('about', about_page, name='about page'),
    path('anime/', anime_page, name='anime page'),
    path('anime/', include(
        [
            path('details/', anime_details, name='anime details page'),
            path('create/', anime_create, name='anime create page'),
            path('edit/', anime_edit, name='anime edit page'),
            path('delete/', anime_delete, name='anime delete page'),
        ]
    )),
    path('photo/details', photo_details, name='photo details'),
    path('errorpage/', error_404, name='error page')

)
