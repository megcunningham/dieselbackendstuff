# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0002_auto_20151209_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_group',
            field=models.ForeignKey(to='diets.FoodGroup'),
        ),
    ]
