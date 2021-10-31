from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import AddPostForm
from django.views.generic import ListView, DeleteView, CreateView


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


class WomenIndex(ListView):
    model = Women
    template_name = 'women/index.html'  # Задаем маршрут к шаблону вместо стандартного
    context_object_name = 'post'  # Задаем имя списка вместо стандартного

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)  # Выбираем что отображать из списка Women

# def index(request):
#     post = Women.objects.all()
#
#     context = {
#                 'menu': menu,
#                 'post': post,
#                 'title': 'Главная страница',
#                 'cat_selected': 0,
#                 }
#     return render(request, 'women/index.html', context=context)


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


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

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


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'women/post.html', context=context)

class WomenCategory(ListView):
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

# def show_category(request, cat_slug):
#     post = Women.objects.filter(cat__slug=cat_slug)
#
#     # if cat_slug > 3:
#     #     return HttpResponse('Категория не найдена')
#
#     context = {
#                 'menu': menu,
#                 'post': post,
#                 'title': f'Категории',
#                 'cat_selected': cat_slug,
#                 }
#     return render(request, 'women/index.html', context=context)
#
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
