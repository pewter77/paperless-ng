# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 19:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('documents', '0010_log'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sender',
            new_name='Correspondent',
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ('correspondent', 'title')},
        ),
        migrations.RenameField(
            model_name='document',
            old_name='sender',
            new_name='correspondent',
        ),
    ]
