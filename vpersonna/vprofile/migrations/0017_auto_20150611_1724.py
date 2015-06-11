# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0016_auto_20150609_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brutepacket',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
