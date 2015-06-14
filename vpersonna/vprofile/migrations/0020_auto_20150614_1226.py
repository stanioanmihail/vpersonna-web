# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('vprofile', '0019_auto_20150613_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(unique=True, max_length=100, verbose_name=b'Email', validators=[django.core.validators.RegexValidator(regex=b'^\\w[^@]*@\\w[^@.]+.\\w[^.]{2,4}$', message=b'Wrong email format!')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.CharField(unique=True, max_length=20, verbose_name=b'Username ', validators=[django.core.validators.RegexValidator(regex=b'^[a-z0-9_\\.]{3,16}$', message=b'Username contains just digits, letters and _')]),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.CharField(max_length=512, verbose_name=b'News Content'),
        ),
    ]
