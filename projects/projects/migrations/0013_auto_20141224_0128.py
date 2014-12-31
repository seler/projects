# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20141224_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='note',
            field=models.TextField(default=b'this is your notepad...', verbose_name='note'),
            preserve_default=True,
        ),
    ]
