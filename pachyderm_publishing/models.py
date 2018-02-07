from django.db import models
import operator


class Genre(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name


class Author(models.Model):
    '''
    author_formatted_name will be written in last name, first name format in order
    to go by last name.

    author_name will be the normal listing on the book page.

    For more than one author on book: author_formatted_name, authors will be
    separated by semi-colon and author_name will be separated by '&'.
    '''
    author_name = models.CharField(max_length=100)
    author_formatted_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    book_genre = models.ForeignKey(Genre)
    book_author = models.ForeignKey(Author)
    book_title = models.CharField(max_length=100)
    book_year = models.IntegerField()
    book_synopsis = models.TextField(blank=True)
    book_cover = models.ImageField(upload_to='book_covers')
    amazon_link = models.CharField(max_length=100, blank=True)

    def average_rating(self):
        all_ratings = list(map(operator.attrgetter("rating"), self.review_set.all()))
        return sum(all_ratings) / len(all_ratings)

    def __str__(self):
        return self.book_title


class Review(models.Model):
    RATING_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )
    book = models.ForeignKey(Book)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    book_review_title = models.CharField(max_length=200)
    book_review = models.TextField(blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.book_review_title
