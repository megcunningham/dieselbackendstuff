# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('body_fat', models.CharField(blank=True, max_length=40)),
                ('weight', models.CharField(null=True, blank=True, max_length=3)),
                ('show', models.CharField(blank=True, max_length=100)),
                ('weeks_out', models.CharField(null=True, blank=True, max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('stats', models.ForeignKey(to='diets.ClientStat')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('food', models.CharField(unique=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('food_group', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('meal_number', models.CharField(blank=True, max_length=50)),
                ('diet', models.ForeignKey(to='diets.Diet')),
            ],
        ),
        migrations.CreateModel(
            name='MeasureServing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('serving_size', models.CharField(blank=True, max_length=50)),
                ('diet', models.ForeignKey(to='diets.Diet')),
                ('food', models.ForeignKey(blank=True, to='diets.Food')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='servings',
            field=models.ForeignKey(to='diets.MeasureServing'),
        ),
        migrations.AddField(
            model_name='food',
            name='food_group',
            field=models.ForeignKey(to='diets.FoodGroup'),
        ),
    ]
