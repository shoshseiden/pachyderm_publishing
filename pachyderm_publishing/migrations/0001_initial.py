# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author_name', models.CharField(max_length=50)),
                ('author_formatted_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_title', models.CharField(max_length=100)),
                ('book_year', models.IntegerField()),
                ('book_synopsis', models.TextField(blank=True)),
                ('book_cover', models.ImageField(upload_to=b'book_covers')),
                ('amazon_link', models.CharField(max_length=100, blank=True)),
                ('book_author', models.ForeignKey(to='pachyderm_publishing.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('user_name', models.CharField(max_length=100)),
                ('book_review_title', models.CharField(max_length=200)),
                ('book_review', models.TextField(blank=True)),
                ('rating', models.IntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('book', models.ForeignKey(to='pachyderm_publishing.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_genre',
            field=models.ForeignKey(to='pachyderm_publishing.Genre'),
        ),
    ]
