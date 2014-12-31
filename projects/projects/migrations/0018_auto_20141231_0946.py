# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20141231_0933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='component',
            options={'verbose_name': 'component', 'verbose_name_plural': 'components'},
        ),
        migrations.RemoveField(
            model_name='component',
            name='order',
        ),
    ]
