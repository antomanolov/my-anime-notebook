from django.shortcuts import render


def index_page(request):
    return render(request, 'common/index.html')


def about_page(request):
    return render(request, 'common/about.html')



def photo_details(request):
    return render(request, 'photo/photo_details.html')


def error_404(request):
    return render(request, '404.html')
