# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-24 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170824_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]