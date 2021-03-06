from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/',views.Booklistview.as_view(), name='book-list'),
    path('book/create/',views.Bookcreateview.as_view(), name='book-create'),
    path('book/delete/<int:pk>', views.Bookdeleteview.as_view(), name='book-delete'),
    path('book/detail/<int:pk>', views.Bookdetailview.as_view(), name='book-detail'),
    path('book/update/<int:pk>', views.Bookupdateview.as_view(), name='book-update'),
    path('genre/',views.Genrelistview.as_view(), name='genre-list'),
    path('genre/create/',views.Genrecreateview.as_view(), name='genre-create'),
    path('genre/delete/<int:pk>', views.Genredeleteview.as_view(), name='genre-delete'),
    path('genre/update/<int:pk>', views.Genreupdateview.as_view(), name='genre-update'),
    path('genre/detail/<int:pk>', views.Genredetailview.as_view(), name='genre-detail'),
    path('author/', views.Authorlistview.as_view(), name='author-list'),
    path('author/create', views.Authorcreateview.as_view(), name='author-create'),
    path('author/delete/<int:pk>', views.Authordeleteview.as_view(), name='author-delete'),
    path('author/detail/<int:pk>', views.Authordetailview.as_view(), name='author-detail'),
    path('author/update/<int:pk>', views.Authorupdateview.as_view(), name='author-update'),
    path('publisher/', views.Publisherlistview.as_view(), name='publisher-list'),
    path('publisher/create', views.Publishercreateview.as_view(), name='publisher-create'),
    path('publisher/delete/<int:pk>', views.Publisherdeleteview.as_view(), name='publisher-delete'),
    path('publisher/detail/<int:pk>', views.Publisherdetailview.as_view(), name='publisher-detail'),
    path('publisher/update/<int:pk>', views.Publisherupdateview.as_view(), name='publisher-update'),
    path('filter/', views.Filter, name='filter'),
]