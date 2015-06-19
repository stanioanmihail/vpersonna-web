# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0024_auto_20150619_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rawpacket',
            name='timestamp_format',
        ),
        migrations.AlterField(
            model_name='rawpacket',
            name='timestamp_end',
            field=models.DateTimeField(verbose_name=b'End session'),
        ),
    ]
