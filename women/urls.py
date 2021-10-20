from django.urls import path

from women.views import index, categories, home

urlpatterns = [
    path('', home),
    path('women/', index),
    path('cats/<int:catid>/', categories),
]
