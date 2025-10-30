from django.urls import path

from . import views

urlpatterns = [
    path('post_list', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('article/new/', views.post_new, name='post_new'),
    path('main_articles/', views.main_articles, name='main_articles'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit')
]