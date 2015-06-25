# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=100, verbose_name=b'Action Description')),
                ('issuer', models.CharField(max_length=100, verbose_name=b'Requestor username')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Client Name')),
                ('phone_number', models.CharField(blank=True, max_length=20, verbose_name=b'Phone Number', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('email', models.EmailField(unique=True, max_length=100, verbose_name=b'Email', validators=[django.core.validators.RegexValidator(regex=b'^\\w[^@]*@\\w[^@.]+.\\w[^.]{2,4}$', message=b'Wrong email format!')])),
                ('card_id', models.CharField(blank=True, max_length=20, verbose_name=b'Card ID', validators=[django.core.validators.RegexValidator(regex=b'^\\d{13}$', message=b'Card ID (CNP) is 13 digits left.')])),
                ('address', models.CharField(max_length=300, verbose_name=b'Address')),
                ('contract_id', models.CharField(max_length=100, verbose_name=b'Contract')),
                ('contract_type', models.CharField(max_length=100, verbose_name=b'Contract Type', blank=True)),
                ('username', models.CharField(unique=True, max_length=20, verbose_name=b'Username ', validators=[django.core.validators.RegexValidator(regex=b'^[a-z0-9_\\.]{3,16}$', message=b'Username contains just digits, letters and _')])),
                ('password', models.CharField(max_length=50, verbose_name=b'Password ')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IPAllocation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ip_addr', models.CharField(max_length=20, verbose_name=b'IP address ', validators=[django.core.validators.RegexValidator(regex=b'^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$', message=b'IP format A.B.C.D')])),
                ('client', models.ForeignKey(to='vprofile.Client')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=25, verbose_name=b'News Title')),
                ('content', models.CharField(max_length=4096, verbose_name=b'News Content')),
                ('active', models.BooleanField(verbose_name=b'Active/Hidden')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('offer_id', models.AutoField(serialize=False, primary_key=True)),
                ('offer_name', models.CharField(max_length=25, verbose_name=b'Offer Name')),
                ('offer_description', models.CharField(max_length=25, verbose_name=b'Offer description', blank=True)),
                ('offer_short_description', models.CharField(max_length=200, verbose_name=b'Offer short description', blank=True)),
                ('cost_per_min', models.PositiveIntegerField(verbose_name=b'Cost per minute')),
            ],
        ),
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ip_src', models.CharField(max_length=20, verbose_name=b'Source IP address ', validators=[django.core.validators.RegexValidator(regex=b'^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$', message=b'IP format A.B.C.D')])),
                ('ip_dst', models.CharField(max_length=20, verbose_name=b'Destination IP address ', validators=[django.core.validators.RegexValidator(regex=b'^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$', message=b'IP format A.B.C.D')])),
                ('port_src', models.PositiveIntegerField(verbose_name=b'Source Port Value')),
                ('port_dst', models.PositiveIntegerField(verbose_name=b'Destination Port Value')),
                ('transport_protocol', models.CharField(max_length=7, verbose_name=b'Transport Layer Protocol', blank=True)),
                ('host_address', models.CharField(max_length=50, verbose_name=b'HTTP Host', blank=True)),
                ('traffic_type', models.CharField(max_length=10, verbose_name=b'Traffic Type')),
                ('timestamp_start', models.DateTimeField(verbose_name=b'Start session')),
                ('timestamp_end', models.DateTimeField(verbose_name=b'End session')),
                ('no_bytes', models.PositiveIntegerField(verbose_name=b'Total bytes number')),
                ('no_packets', models.PositiveIntegerField(verbose_name=b'Total packets number')),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('rule_id', models.AutoField(serialize=False, primary_key=True)),
                ('bandwidth_percent', models.PositiveIntegerField(verbose_name=b'Bandwidth Percent')),
                ('destination_address', models.CharField(max_length=b'200', verbose_name=b'Destination URL', blank=True)),
                ('client', models.ForeignKey(to='vprofile.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('service_id', models.AutoField(serialize=False, primary_key=True)),
                ('service_name', models.CharField(max_length=25, verbose_name=b'Service name')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceUtilizationStatistics',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField()),
                ('num_accesses', models.PositiveIntegerField(verbose_name=b'Number of sessions')),
                ('client', models.ForeignKey(to='vprofile.Client')),
                ('service', models.ForeignKey(to='vprofile.ServiceType')),
            ],
        ),
        migrations.CreateModel(
            name='SiteAccess',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('url', models.CharField(max_length=25, verbose_name=b'Site URL', blank=True)),
                ('num_accesses', models.PositiveIntegerField(verbose_name=b'Number of sessions')),
            ],
        ),
        migrations.AddField(
            model_name='rule',
            name='type_of_service',
            field=models.ForeignKey(to='vprofile.ServiceType'),
        ),
        migrations.AddField(
            model_name='activity',
            name='client',
            field=models.ForeignKey(to='vprofile.Client'),
        ),
    ]
