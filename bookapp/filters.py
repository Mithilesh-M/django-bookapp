import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'no_of_page', 'genre', 'publisher', 'author','published_date']
