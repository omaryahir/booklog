# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20150323_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_file',
            field=models.FileField(upload_to=b'media/books'),
            preserve_default=True,
        ),
    ]
