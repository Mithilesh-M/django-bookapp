from django.shortcuts import render
from .models import Book, Genre, Publisher, Author
from django.views import generic
from django.urls import reverse_lazy

def index(request):
    context = {
        'book': Book.objects.all().count(),
        'genre': Genre.objects.all().count(),
        'publisher': Publisher.objects.all().count(),
        'author': Author.objects.all().count(),
    }
    return render(request, 'bookapp/index.html', context)


class Booklistview(generic.ListView):
    model = Book

class Bookcreateview(generic.CreateView):
    model = Book
    fields = ['title','no_of_page','cover_image','description','genre','publisher','author','published_date']
    success_url = reverse_lazy('book-list')

class Genrelistview(generic.ListView):
    model = Genre

class Genrecreateview(generic.CreateView):
    model = Genre
    fields = ['name']
    success_url = reverse_lazy('genre-list')

class Authorlistview(generic.ListView):
    model = Author

class Authorcreateview(generic.CreateView):
    model = Author
    fields = ['name','bio','phone']
    success_url = reverse_lazy('author-list')
