from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/',views.Booklistview.as_view(), name='book-list'),
]