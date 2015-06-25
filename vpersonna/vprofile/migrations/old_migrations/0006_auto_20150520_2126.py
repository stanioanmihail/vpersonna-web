# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0005_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offer_short_description',
            field=models.CharField(max_length=200, verbose_name=b'Offer short description', blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_description',
            field=models.CharField(max_length=25, verbose_name=b'Offer description', blank=True),
        ),
    ]
