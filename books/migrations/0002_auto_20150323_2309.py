# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('editorial', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default='', to='authors.Author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='editorial',
            field=models.ForeignKey(default='', to='editorial.Editorial'),
            preserve_default=False,
        ),
    ]
