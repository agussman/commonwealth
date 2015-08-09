# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commonwealth', '0003_auto_20150808_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='transportation_score',
            field=models.IntegerField(default=0),
        ),
    ]
