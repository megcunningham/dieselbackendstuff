# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now, help_text='Created on')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('food', models.CharField(blank=True, max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('food_group', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('meal_number', models.CharField(blank=True, max_length=50, help_text='Notes')),
                ('food', models.ForeignKey(blank=True, to='diets.Food')),
            ],
        ),
        migrations.CreateModel(
            name='MeasureServing',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('serving_size', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('quantity', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ClientStat',
            fields=[
                ('date_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, primary_key=True, to='diets.Date')),
                ('name', models.CharField(max_length=150)),
                ('body_fat', models.CharField(blank=True, max_length=40)),
                ('weight', models.CharField(blank=True, max_length=3, null=True)),
                ('show', models.CharField(blank=True, max_length=100)),
                ('weeks_out', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('diets.date',),
        ),
        migrations.AddField(
            model_name='meal',
            name='quantity',
            field=models.ForeignKey(blank=True, to='diets.Quantity'),
        ),
        migrations.AddField(
            model_name='meal',
            name='serving_size',
            field=models.ForeignKey(to='diets.MeasureServing', null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='food_group',
            field=models.ForeignKey(to='diets.FoodGroup'),
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('clientstat_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, primary_key=True, to='diets.ClientStat')),
                ('notes', models.TextField(help_text='Trainer notes')),
            ],
            bases=('diets.clientstat',),
        ),
        migrations.AddField(
            model_name='meal',
            name='diet',
            field=models.ForeignKey(to='diets.Diet'),
        ),
    ]
