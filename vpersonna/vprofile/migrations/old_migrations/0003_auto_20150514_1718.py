# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0002_auto_20150514_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='id',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='id',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='id',
        ),
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.IntegerField(serialize=False, verbose_name=b'Client ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='rule_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='service_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
