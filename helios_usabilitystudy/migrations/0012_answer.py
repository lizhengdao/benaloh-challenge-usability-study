# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-15 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helios_usabilitystudy', '0011_auto_20180815_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sus_one', models.IntegerField(verbose_name='SUS One')),
                ('sus_two', models.IntegerField(verbose_name='SUS Two')),
                ('sus_three', models.IntegerField(verbose_name='SUS Three')),
                ('sus_four', models.IntegerField(verbose_name='SUS Four')),
                ('sus_five', models.IntegerField(verbose_name='SUS Five')),
                ('sus_six', models.IntegerField(verbose_name='SUS Six')),
                ('sus_seven', models.IntegerField(verbose_name='SUS Seven')),
                ('sus_eight', models.IntegerField(verbose_name='SUS Eight')),
                ('sus_nine', models.IntegerField(verbose_name='SUS Nine')),
                ('sus_ten', models.IntegerField(verbose_name='SUS Ten')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='helios_usabilitystudy.Subject')),
            ],
        ),
    ]