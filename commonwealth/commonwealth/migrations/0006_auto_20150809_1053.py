# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commonwealth', '0005_auto_20150808_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='actual_wage',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='business',
            name='coin_score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='business',
            name='transportation_score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='business',
            name='wage_score',
            field=models.FloatField(default=0.0),
        ),
    ]
