# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 02:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vdnapp', '0005_auto_20170405_0237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annotation',
            old_name='server',
            new_name='vdn_server',
        ),
    ]
