# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField(verbose_name='body')),
            ],
            options={
                'verbose_name': 'note',
                'verbose_name_plural': 'notes',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='component',
            name='order',
            field=models.PositiveSmallIntegerField(default=None, verbose_name='order', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='managers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='managers', blank=True),
            preserve_default=True,
        ),
    ]
