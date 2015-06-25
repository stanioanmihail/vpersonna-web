# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0009_auto_20150601_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='client',
            field=models.IntegerField(),
        ),
    ]
