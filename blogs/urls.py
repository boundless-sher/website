from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs_list, name='blogs-list'),
    path('hx-blogs-list/', views.hx_blogs_list, name='hx-blogs-list'),
    path('<str:blog_slug>/', views.blog_detail, name='blog-detail'),
]
