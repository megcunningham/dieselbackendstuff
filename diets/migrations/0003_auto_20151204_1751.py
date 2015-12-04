# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0002_auto_20151204_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food',
            field=models.CharField(max_length=25, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='food',
            field=models.ForeignKey(to='diets.Food', null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='quantity',
            field=models.ForeignKey(blank=True, to='diets.Quantity'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='serving_size',
            field=models.ForeignKey(to='diets.MeasureServing', null=True),
        ),
        migrations.AlterField(
            model_name='measureserving',
            name='serving_size',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='quantity',
            name='quantity',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
