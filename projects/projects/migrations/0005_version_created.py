# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20140918_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 18, 19, 43, 38, 483384), verbose_name='created', editable=False),
            preserve_default=False,
        ),
    ]
