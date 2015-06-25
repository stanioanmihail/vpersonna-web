# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rule_id', models.IntegerField(verbose_name=b'Rule id')),
                ('bandwidth_percent', models.IntegerField(verbose_name=b'Bandwidth Percent')),
                ('destination_address', models.CharField(max_length=b'200', verbose_name=b'Destination URL', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_id', models.IntegerField(verbose_name=b'Service id')),
                ('service_name', models.CharField(max_length=25, verbose_name=b'Service name')),
            ],
        ),
        migrations.AddField(
            model_name='rule',
            name='type_of_service',
            field=models.ForeignKey(to='vprofile.ServiceType'),
        ),
    ]
