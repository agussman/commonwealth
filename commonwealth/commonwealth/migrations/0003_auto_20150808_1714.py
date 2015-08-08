# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commonwealth', '0002_business_yelp_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='overall_score',
            new_name='coin_score',
        ),
        migrations.RemoveField(
            model_name='business',
            name='certification_level',
        ),
        migrations.AddField(
            model_name='business',
            name='actual_wage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='business',
            name='address',
            field=models.TextField(default='no address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='business_name',
            field=models.CharField(max_length=200, default='no name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='image_url',
            field=models.CharField(max_length=500, default='no image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='wage_score',
            field=models.IntegerField(default=0),
        ),
    ]
