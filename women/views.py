from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
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
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True)  # Выбираем что отображать из списка Women


def about(request):
    context = {
                'menu': menu,
                'title': 'О сайте'
                }
    return render(request, 'women/about.html', context=context)

class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('index')  # Выбираем куда нас перенаправить миксин LoginRequiredMixin
    raise_exception = True # Выбираем исключение для миксина LoginRequiredMixin

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))


def contact(request):
    return HttpResponse('Обратная связь')

# def login(request):
#     return HttpResponse('Авторизация')

class ShowPost(DataMixin, DeleteView):
    model = Women
    template_name = 'women/post.html'  # Задаем маршрут к шаблону вместо стандартного
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'  # Задаем имя списка вместо стандартного

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'  # Задаем маршрут к шаблону вместо стандартного
    context_object_name = 'post'  # Задаем имя списка вместо стандартного
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Категория - " + str(context['post'][0].cat), cat_selected=context['post'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)  # Выбираем что отображать из списка Women

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')  # Перенаправление при успешной регистрации

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):  # логинит при успешной регистрации
        user = form.save()
        login(self.request, user)  # специальная функция которая авторизовывает пользователя, импорт
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')  # Можем заменить LOGIN_REDIRECT_URL ='/' в settings.py

def logout_user(request):
    logout(request)
    return redirect('login')