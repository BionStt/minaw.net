# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perso', '0004_auto_20170705_1537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['menu', 'id'], 'verbose_name': 'catégorie'},
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.BooleanField(default=True),
        ),
    ]
