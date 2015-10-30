# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0017_auto_20151028_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseset',
            name='number_of_sets',
            field=models.CharField(max_length=30),
        ),
    ]
