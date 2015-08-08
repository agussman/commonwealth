# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commonwealth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='yelp_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
