from django.urls import path
from . import views

urlpatterns = [
  path('', views.link_list, name='links'),
  path('hx-links/', views.hx_links, name='hx-links'),
]