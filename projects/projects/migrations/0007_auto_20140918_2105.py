# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20140918_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='component',
            field=models.ForeignKey(verbose_name='component', to='projects.Component', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='file',
            name='layer',
            field=models.ForeignKey(verbose_name='layer', to='projects.Layer', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='file',
            name='project',
            field=models.ForeignKey(verbose_name='project', to='projects.Project', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.URLField(verbose_name='url'),
        ),
    ]
