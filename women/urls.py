from django.urls import path

from women.views import index, categories, about

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('cats/<int:catid>/', categories, name='cats'),
]
