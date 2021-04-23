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
    fields = ['title','isbn','no_of_page','cover_image','description','genre','publisher','author','published_date']
    success_url = reverse_lazy('book-list')

class Bookdeleteview(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')

class Bookdetailview(generic.DetailView):
    model = Book

class Bookupdateview(generic.UpdateView):
    model = Book
    fields = fields = ['title','isbn','no_of_page','cover_image','description','genre','publisher','author','published_date']
    success_url = reverse_lazy('book-list')

class Genrelistview(generic.ListView):
    model = Genre

class Genrecreateview(generic.CreateView):
    model = Genre
    fields = ['name']
    success_url = reverse_lazy('genre-list')

class Genredeleteview(generic.DeleteView):
    model = Genre
    success_url = reverse_lazy('genre-list')

class Authorlistview(generic.ListView):
    model = Author

class Authorcreateview(generic.CreateView):
    model = Author
    fields = ['name','bio','phone']
    success_url = reverse_lazy('author-list')

class Authordeleteview(generic.DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')

class Publisherlistview(generic.ListView):
    model = Publisher

class Publishercreateview(generic.CreateView):
    model = Publisher
    fields = ['name','address','description','phone']
    success_url = reverse_lazy('publisher-list')

class Publisherdeleteview(generic.DeleteView):
    model = Publisher
    success_url = reverse_lazy('publisher-list')

