# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editorial', '0002_auto_20150325_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorial',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'editorial', blank=True),
            preserve_default=True,
        ),
    ]
