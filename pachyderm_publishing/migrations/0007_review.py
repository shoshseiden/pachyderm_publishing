# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pachyderm_publishing', '0006_auto_20161111_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('user_name', models.CharField(max_length=100)),
                ('book_review', models.TextField(blank=True)),
                ('book_rating', models.IntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('book', models.ForeignKey(to='pachyderm_publishing.Book')),
            ],
        ),
    ]
