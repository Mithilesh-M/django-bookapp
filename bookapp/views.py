from django.shortcuts import render
from .models import Book, Genre, Publisher, Author
from django.views import generic

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
