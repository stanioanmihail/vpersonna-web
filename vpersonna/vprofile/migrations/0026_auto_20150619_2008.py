# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0025_auto_20150619_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawpacket',
            name='timestamp_start',
            field=models.DateTimeField(verbose_name=b'Start session'),
        ),
    ]
