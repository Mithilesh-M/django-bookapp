from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/',views.Booklistview.as_view(), name='book-list'),
    path('book/create/',views.Bookcreateview.as_view(), name='book-create'),
    path('book/delete/<int:pk>', views.Bookdeleteview.as_view(), name='book-delete'),
    path('genre/',views.Genrelistview.as_view(), name='genre-list'),
    path('genre/create/',views.Genrecreateview.as_view(), name='genre-create'),
    path('genre/delete/<int:pk>', views.Genredeleteview.as_view(), name='genre-delete'),
    path('author/', views.Authorlistview.as_view(), name='author-list'),
    path('author/create', views.Authorcreateview.as_view(), name='author-create'),
    path('publisher/', views.Publisherlistview.as_view(), name='publisher-list'),
    path('publisher/create', views.Publishercreateview.as_view(), name='publisher-create'),
]