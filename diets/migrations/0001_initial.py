# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carbohydrate',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('carbohydrates', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fat',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('fats', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('carbohydrates', models.ForeignKey(to='diets.Carbohydrate', blank=True)),
                ('fats', models.ForeignKey(to='diets.Fat', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Green',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('greens', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('meal', models.CharField(max_length=50, unique=True)),
                ('food', models.ForeignKey(to='diets.Food', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewDiet',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('meal_number', models.ForeignKey(to='diets.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Protein',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('protein', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Serving',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('serving_size', models.CharField(max_length=50, blank=True)),
                ('measurement', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('body_fat', models.CharField(max_length=40)),
                ('show', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='protein',
            name='serving',
            field=models.ForeignKey(null=True, to='diets.Serving'),
        ),
        migrations.AddField(
            model_name='newdiet',
            name='stats',
            field=models.ForeignKey(to='diets.Stat'),
        ),
        migrations.AddField(
            model_name='green',
            name='serving',
            field=models.ForeignKey(null=True, to='diets.Serving'),
        ),
        migrations.AddField(
            model_name='food',
            name='greens',
            field=models.ForeignKey(to='diets.Green', blank=True),
        ),
        migrations.AddField(
            model_name='food',
            name='protein',
            field=models.ForeignKey(to='diets.Protein', blank=True),
        ),
        migrations.AddField(
            model_name='fat',
            name='serving',
            field=models.ForeignKey(null=True, to='diets.Serving'),
        ),
        migrations.AddField(
            model_name='carbohydrate',
            name='serving',
            field=models.ForeignKey(null=True, to='diets.Serving'),
        ),
    ]
