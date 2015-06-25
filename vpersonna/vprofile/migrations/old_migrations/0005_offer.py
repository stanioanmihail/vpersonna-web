# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0004_auto_20150515_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('offer_id', models.AutoField(serialize=False, primary_key=True)),
                ('offer_name', models.CharField(max_length=25, verbose_name=b'Offer Name')),
                ('offer_description', models.CharField(max_length=200, verbose_name=b'Offer description', blank=True)),
                ('cost_per_min', models.PositiveIntegerField(verbose_name=b'Cost per minute')),
            ],
        ),
    ]
