# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0005_auto_20151001_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='DifficultyLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='workout',
            name='level',
            field=models.ForeignKey(to='workouts.DifficultyLevel', default=1),
            preserve_default=False,
        ),
    ]
