# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0027_auto_20150619_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.CharField(max_length=4096, verbose_name=b'News Content'),
        ),
    ]
