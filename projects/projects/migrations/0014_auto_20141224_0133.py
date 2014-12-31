# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20141224_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='note',
        ),
        migrations.AddField(
            model_name='component',
            name='notepad',
            field=models.TextField(default=b'this is your notepad...', verbose_name='notepad'),
            preserve_default=True,
        ),
    ]
