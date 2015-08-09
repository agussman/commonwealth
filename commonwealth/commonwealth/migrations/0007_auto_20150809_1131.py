# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commonwealth', '0006_auto_20150809_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='yelp_id',
            field=models.CharField(max_length=200),
        ),
    ]
