# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commonwealth', '0004_business_transportation_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='lat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='business',
            name='lon',
            field=models.FloatField(default=0.0),
        ),
    ]
