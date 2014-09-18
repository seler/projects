# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_version_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ('-created',), 'get_latest_by': 'created', 'verbose_name': 'version', 'verbose_name_plural': 'versions'},
        ),
        migrations.RenameField(
            model_name='item',
            old_name='link',
            new_name='url',
        ),
    ]
