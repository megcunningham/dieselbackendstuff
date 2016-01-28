# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='meal_number',
        ),
        migrations.AddField(
            model_name='meal',
            name='note',
            field=models.CharField(help_text='Meal No.', blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='clientstat',
            name='body_fat',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='clientstat',
            name='show',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientstat',
            name='weight',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='food',
            field=models.CharField(blank=True, max_length=25, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_group',
            field=models.ForeignKey(verbose_name='Related Lookup (FK)', to='diets.FoodGroup'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='food',
            field=models.ForeignKey(blank=True, null=True, to='diets.Food'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='quantity',
            field=models.ForeignKey(blank=True, null=True, to='diets.Quantity'),
        ),
    ]
