# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.IntegerField(verbose_name=b'Client ID')),
                ('client_name', models.CharField(max_length=200, verbose_name=b'Client Name')),
                ('phone_number', models.CharField(blank=True, max_length=20, verbose_name=b'Phone Number', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('email', models.EmailField(max_length=100, verbose_name=b'Email')),
                ('card_id', models.CharField(blank=True, max_length=20, verbose_name=b'Card ID', validators=[django.core.validators.RegexValidator(regex=b'^\\d{13}$', message=b'Card ID (CNP) is 13 digits left.')])),
                ('address', models.CharField(max_length=300, verbose_name=b'Address')),
                ('contract_id', models.CharField(max_length=100, verbose_name=b'Contract')),
                ('contract_type', models.CharField(max_length=100, verbose_name=b'Contract Type')),
                ('username', models.CharField(blank=True, max_length=20, verbose_name=b'Username ', validators=[django.core.validators.RegexValidator(regex=b'^[a-z0-9_]{3,16}$', message=b'Username contains just digits, letters and _')])),
                ('password', models.CharField(max_length=20, verbose_name=b'Password ', blank=True)),
            ],
        ),
    ]
