# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0023_auto_20150619_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawpacket',
            name='timestamp_format',
            field=models.CharField(default='%d-%m-%Y %H:%M', max_length=50, verbose_name=b'Timestamp format'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rawpacket',
            name='timestamp_end',
            field=models.CharField(max_length=50, verbose_name=b'End session date'),
        ),
        migrations.AlterField(
            model_name='rawpacket',
            name='timestamp_start',
            field=models.CharField(max_length=50, verbose_name=b'Start session date'),
        ),
        migrations.AlterField(
            model_name='rawpacket',
            name='transport_protocol',
            field=models.CharField(max_length=7, verbose_name=b'Transport Layer Protocol', blank=True),
        ),
    ]
