# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0015_brutepacket_transport_protocol'),
    ]

    operations = [
        migrations.AddField(
            model_name='brutepacket',
            name='host_address',
            field=models.CharField(max_length=50, verbose_name=b'HTTP Host', blank=True),
        ),
        migrations.AddField(
            model_name='brutepacket',
            name='traffic_type',
            field=models.CharField(default='Default', max_length=10, verbose_name=b'Traffic Type'),
            preserve_default=False,
        ),
    ]
