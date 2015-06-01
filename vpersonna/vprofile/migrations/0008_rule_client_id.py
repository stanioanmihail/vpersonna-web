# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0007_auto_20150601_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='client_id',
            field=models.ForeignKey(default=1, to='vprofile.Client'),
            preserve_default=False,
        ),
    ]
