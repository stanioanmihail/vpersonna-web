# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0022_auto_20150615_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawPacket',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ip_src', models.CharField(max_length=20, verbose_name=b'Source IP address ', validators=[django.core.validators.RegexValidator(regex=b'^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$', message=b'IP format A.B.C.D')])),
                ('ip_dst', models.CharField(max_length=20, verbose_name=b'Destination IP address ', validators=[django.core.validators.RegexValidator(regex=b'^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$', message=b'IP format A.B.C.D')])),
                ('port_src', models.PositiveIntegerField(verbose_name=b'Source Port Value')),
                ('port_dst', models.PositiveIntegerField(verbose_name=b'Destination Port Value')),
                ('transport_protocol', models.BooleanField(verbose_name=b'Transport Layer Protocol: 0-UDP, 1-TCP')),
                ('host_address', models.CharField(max_length=50, verbose_name=b'HTTP Host', blank=True)),
                ('traffic_type', models.CharField(max_length=10, verbose_name=b'Traffic Type')),
                ('timestamp_start', models.DateTimeField(verbose_name=b'Start session')),
                ('timestamp_end', models.DateTimeField(verbose_name=b'End session')),
                ('nb_bytes', models.PositiveIntegerField(verbose_name=b'Total bytes number')),
            ],
        ),
        migrations.DeleteModel(
            name='BrutePacket',
        ),
    ]
