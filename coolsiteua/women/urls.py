from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.decorators.cache import cache_page

handler404 = pageNotFound

urlpatterns = [
    path('', cache_page(60)(WomenHome.as_view()), name='home'),
    path('cats/<slug:cat_slug>', WomenCategory.as_view(), name='category'),
    path('about/', about, name='about'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('contact/', contact,name='contact'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]