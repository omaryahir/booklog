# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorial',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'media/editorial', blank=True),
            preserve_default=True,
        ),
    ]
