# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0008_rule_client_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rule',
            old_name='client_id',
            new_name='client',
        ),
    ]
