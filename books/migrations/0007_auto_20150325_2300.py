# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20150325_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_file',
        ),
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default='', upload_to=b'files/books'),
            preserve_default=False,
        ),
    ]
