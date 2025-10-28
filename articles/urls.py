from django.urls import path

from . import views

urlpatterns = [
    path('post_list', views.post_list, name='post_list'),
    path('main_articles/', views.main_articles, name='main_articles'),
]