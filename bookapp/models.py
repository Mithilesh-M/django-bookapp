from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Enter book title")
    isbn = models.UUIDField(unique=True)
    no_of_page = models.DecimalField("Enter no.of page",decimal_places=0,max_digits=6)
    cover_image = models.ImageField()
    description = models.TextField(max_length=500, help_text="Enter description")
    genre = models.ManyToManyField('Genre')
    publisher = models.ManyToManyField('Publisher')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True)
    published_date = models.DateField()

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter genre name")

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=200, help_text="Enter genre name")
    address = models.CharField(max_length=500, help_text="Enter address")
    description = models.TextField(max_length=500, help_text="Enter description")
    phone = models.DecimalField(decimal_places=0, max_digits=10)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the name")
    bio = models.TextField(max_length=500, help_text="Enter bio")
    phone = models.DecimalField(decimal_places=0, max_digits=10)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
