# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pachyderm_publishing', '0007_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book_review_title',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
