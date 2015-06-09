# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0014_brutepacket_ipallocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='brutepacket',
            name='transport_protocol',
            field=models.BooleanField(default=0, verbose_name=b'Transport Layer Protocol: 0-UDP, 1-TCP'),
            preserve_default=False,
        ),
    ]
