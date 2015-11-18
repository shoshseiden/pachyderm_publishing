# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pachyderm_publishing', '0003_auto_20151118_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(upload_to=b'book_covers'),
        ),
    ]
