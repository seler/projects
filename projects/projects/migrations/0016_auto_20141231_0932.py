# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20141231_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='level',
        ),
        migrations.RemoveField(
            model_name='project',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='project',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='project',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tree_id',
        ),
    ]
