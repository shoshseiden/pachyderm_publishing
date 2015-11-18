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
                ('book_cover', models.ImageField(upload_to=b'book_covers')),
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
        migrations.AddField(
            model_name='book',
            name='book_genre',
            field=models.ForeignKey(to='pachyderm_publishing.Genre'),
        ),
    ]
