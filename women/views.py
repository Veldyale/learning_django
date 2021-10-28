from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


def index(request):
    post = Women.objects.all()

    context = {
                'menu': menu,
                'post': post,
                'title': 'Главная страница',
                'cat_selected': 'cat_slug',
                }
    return render(request, 'women/index.html', context=context)


def about(request):
    context = {
                'menu': menu,
                'title': 'О сайте'
                }
    return render(request, 'women/about.html', context=context)

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.slug,
    }
    return render(request, 'women/post.html', context=context)

def show_category(request, cat_slug):
    post = Women.objects.filter(cat__slug=cat_slug)

    # if cat_slug > 3:
    #     return HttpResponse('Категория не найдена')

    context = {
                'menu': menu,
                'post': post,
                'title': f'Категории',
                'cat_selected': cat_slug,
                }
    return render(request, 'women/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
