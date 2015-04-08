# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20150325_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 21, 22, 19, 315090)),
            preserve_default=True,
        ),
    ]
