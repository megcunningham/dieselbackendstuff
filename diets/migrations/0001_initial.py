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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150)),
                ('body_fat', models.CharField(max_length=40, blank=True)),
                ('weight', models.CharField(max_length=3, null=True, blank=True)),
                ('show', models.CharField(max_length=100, blank=True)),
                ('weeks_out', models.CharField(max_length=3, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('food', models.CharField(unique=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('food_group', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='MeasureServing',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('serving_size', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('quantity', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('clientstat_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, auto_created=True, to='diets.ClientStat')),
                ('date', models.CharField(max_length=30)),
            ],
            bases=('diets.clientstat',),
        ),
        migrations.CreateModel(
            name='MealNumber',
            fields=[
                ('meal_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, auto_created=True, to='diets.Meal')),
                ('meal_number', models.CharField(max_length=15)),
                ('diet', models.ForeignKey(to='diets.Diet')),
            ],
            bases=('diets.meal',),
        ),
        migrations.AddField(
            model_name='meal',
            name='food',
            field=models.ForeignKey(blank=True, to='diets.Food'),
        ),
        migrations.AddField(
            model_name='meal',
            name='quantity',
            field=models.ForeignKey(to='diets.Quantity'),
        ),
        migrations.AddField(
            model_name='meal',
            name='serving_size',
            field=models.ForeignKey(to='diets.MeasureServing'),
        ),
        migrations.AddField(
            model_name='food',
            name='food_group',
            field=models.ForeignKey(to='diets.FoodGroup'),
        ),
    ]
