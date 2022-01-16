from django.urls import path
from blogApp import views

# Listado de views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.pages, name='pages'),
    path('form/', views.formBlog, name='formBlog'),
    path('search/', views.search, name='search'),
    path('search_action/', views.search_action, name='search_action'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]




