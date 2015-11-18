# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pachyderm_publishing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_synopsis',
            field=models.TextField(blank=True),
        ),
    ]
