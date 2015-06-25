# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0006_auto_20150520_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_name',
            new_name='name',
        ),
    ]
