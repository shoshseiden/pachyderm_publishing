# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pachyderm_publishing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_formatted_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='author_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre_name',
            field=models.CharField(max_length=100),
        ),
    ]
