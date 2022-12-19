from django.urls import path, include

from project_defense.web.views import index_page, about_page, photo_details, error_404

urlpatterns = (
    path('', index_page, name='index page'),
    path('about', about_page, name='about page'),

    path('photo/details', photo_details, name='photo details'),
    path('errorpage/', error_404, name='error page')

)
