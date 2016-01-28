from django.db import models


class Genre(models.Model):
    genre_name = models.CharField(max_length=15)

    def __str__(self):
        return self.genre_name


class Author(models.Model):
    '''
    author_formatted_name will be written in last name, first name format in order
    to go by last name.

    author_name will be the normal listing on the book page.
    '''
    author_name = models.CharField(max_length=50)
    author_formatted_name = models.CharField(max_length=50)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    book_genre = models.ForeignKey(Genre)
    book_author = models.ForeignKey(Author)
    book_title = models.CharField(max_length=100)
    book_year = models.IntegerField()
    book_synopsis = models.TextField(blank=True)
    book_cover = models.ImageField(upload_to='book_covers')
    amazon_link = models.CharField(max_length=100)

    def __str__(self):
        return self.book_title
