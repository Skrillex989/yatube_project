from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('Главная страница')


def group_posts(request,slug):
    return HttpResponse(f'Группы мороженого {slug}')
