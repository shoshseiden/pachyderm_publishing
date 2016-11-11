# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pachyderm_publishing', '0005_book_amazon_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='amazon_link',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
