# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0003_auto_20150514_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='bandwidth_percent',
            field=models.PositiveIntegerField(verbose_name=b'Bandwidth Percent'),
        ),
    ]
