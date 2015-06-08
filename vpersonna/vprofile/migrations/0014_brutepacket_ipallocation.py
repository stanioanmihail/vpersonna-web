# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0013_remove_siteaccess_ip_addr'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrutePacket',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ip_src', models.CharField(max_length=20, verbose_name=b'Source IP address ', validators=[django.core.validators.RegexValidator(regex=b'^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$', message=b'IP format A.B.C.D')])),
                ('ip_dst', models.CharField(max_length=20, verbose_name=b'Destination IP address ', validators=[django.core.validators.RegexValidator(regex=b'^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$', message=b'IP format A.B.C.D')])),
                ('port_src', models.PositiveIntegerField(verbose_name=b'Source Port Value')),
                ('port_dst', models.PositiveIntegerField(verbose_name=b'Destination Port Value')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='IPAllocation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ip_addr', models.CharField(max_length=20, verbose_name=b'IP address ', validators=[django.core.validators.RegexValidator(regex=b'^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$', message=b'IP format A.B.C.D')])),
                ('client', models.ForeignKey(to='vprofile.Client')),
            ],
        ),
    ]
