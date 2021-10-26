from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


def index(request):
    posts = Women.objects.all()
    context = {
                'menu': menu,
                'posts': posts,
                'title': 'Главная страница',
                'cat_selected': 0,
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

def show_post(request, post_id):
    posts = Women.objects.all()
    context = {
                'menu': menu,
                'posts': posts,
                'title': 'Пост',
                'post_selected': post_id,
                }
    return render(request, 'women/post.html', context=context)

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if cat_id > 3:
        return HttpResponse('Категория не найдена')

    context = {
                'menu': menu,
                'posts': posts,
                'title': f'Категория {cat_id}',
                'cat_selected': cat_id,
                }
    return render(request, 'women/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
