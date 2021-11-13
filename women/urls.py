from django.urls import path

from women.views import *

urlpatterns = [
    path('', WomenIndex.as_view(), name='index'),
    path('about/', about, name='about'),
    path('addpage/', AddPost.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
]

