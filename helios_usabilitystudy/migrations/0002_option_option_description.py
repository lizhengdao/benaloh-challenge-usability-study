# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helios_usabilitystudy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='option_description',
            field=models.CharField(max_length=2000, null=True, verbose_name='Description'),
        ),
    ]
