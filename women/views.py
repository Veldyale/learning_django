from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from .models import *
from .forms import *
from .utils import *

class WomenIndex(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'  # Задаем маршрут к шаблону вместо стандартного
    context_object_name = 'post'  # Задаем имя списка вместо стандартного

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)  # Выбираем что отображать из списка Women


def about(request):
    context = {
                'menu': menu,
                'title': 'О сайте'
                }
    return render(request, 'women/about.html', context=context)

class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'
        return context


def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

class ShowPost(DeleteView):
    model = Women
    template_name = 'women/post.html'  # Задаем маршрут к шаблону вместо стандартного
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'  # Задаем имя списка вместо стандартного

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'  # Задаем маршрут к шаблону вместо стандартного
    context_object_name = 'post'  # Задаем имя списка вместо стандартного
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['post'][0].cat)
        context['cat_selected'] = context['post'][0].cat_id
        return context


    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)  # Выбираем что отображать из списка Women

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
