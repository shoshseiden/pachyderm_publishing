from django.contrib import admin
from .models import Genre, Author, Book


class BookInline(admin.TabularInline):
    model = Book
    extra = 1


class GenreAdmin(admin.ModelAdmin):
    fields = ['genre_name']
    inlines = [BookInline]


class AuthorAdmin(admin.ModelAdmin):
    fields = ['author_formatted_name', 'author_name']
    inlines = [BookInline]


class BookAdmin(admin.ModelAdmin):
    fieldsets = [('Images', {'fields': ['book_cover']}),
                 ('Book Information', {'fields': ['book_title', 'book_author',
                  'book_year', 'book_genre', 'book_synopsis']}),
                 ('Links', {'fields': ['amazon_link']}),
                ]




admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
