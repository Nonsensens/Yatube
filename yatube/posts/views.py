from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, pk):
    return HttpResponse(f'Пост {pk}')