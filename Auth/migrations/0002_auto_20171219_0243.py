# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-18 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startupfair',
            old_name='angelListUrl',
            new_name='funding',
        ),
        migrations.RenameField(
            model_name='startupfair',
            old_name='crunchBaseUrl',
            new_name='linkUrl',
        ),
        migrations.RemoveField(
            model_name='startupfair',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='startupfair',
            name='pindusry',
        ),
        migrations.AddField(
            model_name='startupfair',
            name='startuptype',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='startupfair',
            name='bType',
            field=models.ManyToManyField(blank=True, null=True, related_name='btype', to='Auth.BusinessType'),
        ),
    ]