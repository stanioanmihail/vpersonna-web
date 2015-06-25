# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0021_auto_20150614_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 17, 16, 2, 732077), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='issuer',
            field=models.CharField(default=1, max_length=100, verbose_name=b'Requestor username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='contract_type',
            field=models.CharField(max_length=100, verbose_name=b'Contract Type', blank=True),
        ),
    ]
