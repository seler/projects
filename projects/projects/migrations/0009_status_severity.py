# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_file_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='severity',
            field=models.CharField(default=b'default', max_length=255, verbose_name='severity', choices=[(b'default', 'deffault'), (b'primary', 'primary'), (b'success', 'success'), (b'info', 'info'), (b'warning', 'warning'), (b'danger', 'danger')]),
            preserve_default=True,
        ),
    ]
