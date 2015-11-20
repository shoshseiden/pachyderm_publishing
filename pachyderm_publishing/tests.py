from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.core.files import File

from .models import Genre, Author, Book


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_genre(self):
        Genre.objects.create(genre_name="test genre")
        url = reverse('genre')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_author(self):
        Author.objects.create(author_formatted_name="Last, First")
        url = reverse('author')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
