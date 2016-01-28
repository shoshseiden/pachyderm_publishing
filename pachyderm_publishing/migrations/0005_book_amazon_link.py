# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pachyderm_publishing', '0004_auto_20151118_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='amazon_link',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
