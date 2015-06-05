# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0011_auto_20150602_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=25, verbose_name=b'News Title')),
                ('content', models.CharField(max_length=255, verbose_name=b'News Content')),
                ('active', models.BooleanField(verbose_name=b'Active/Hidden')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
