from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/',views.Booklistview.as_view(), name='book-list'),
    path('book/create/',views.Bookcreateview.as_view(), name='book-create'),
    path('genre/',views.Genrelistview.as_view(), name='genre-list'),
    path('genre/create/',views.Genrecreateview.as_view(), name='genre-create')
]