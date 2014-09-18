# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20140918_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='version',
            field=models.ForeignKey(verbose_name='version', to='projects.Version', null=True),
            preserve_default=True,
        ),
    ]
