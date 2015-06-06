# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0012_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteaccess',
            name='ip_addr',
        ),
    ]
