# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20141224_0125'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.AddField(
            model_name='component',
            name='note',
            field=models.TextField(default='', verbose_name='note'),
            preserve_default=False,
        ),
    ]
