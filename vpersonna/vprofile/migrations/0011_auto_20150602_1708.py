# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0010_auto_20150601_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=100, verbose_name=b'Action Description')),
                ('client', models.ForeignKey(to='vprofile.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceUtilizationStatistics',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField()),
                ('num_accesses', models.PositiveIntegerField(verbose_name=b'Number of accesses')),
                ('client', models.ForeignKey(to='vprofile.Client')),
                ('service', models.ForeignKey(to='vprofile.ServiceType')),
            ],
        ),
        migrations.CreateModel(
            name='SiteAccess',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('url', models.CharField(max_length=25, verbose_name=b'Site URL', blank=True)),
                ('ip_addr', models.CharField(max_length=20, verbose_name=b'IP address ', validators=[django.core.validators.RegexValidator(regex=b'^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$', message=b'IP format A.B.C.D')])),
                ('num_accesses', models.PositiveIntegerField(verbose_name=b'Number of accesses')),
            ],
        ),
        migrations.AlterField(
            model_name='rule',
            name='client',
            field=models.ForeignKey(to='vprofile.Client'),
        ),
    ]
