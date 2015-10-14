# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0006_auto_20151014_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='level',
        ),
    ]
