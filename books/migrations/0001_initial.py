# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField()),
                ('book_file', models.FileField(upload_to=b'books')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
