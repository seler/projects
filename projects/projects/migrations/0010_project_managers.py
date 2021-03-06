# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0009_status_severity'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='managers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='managers'),
            preserve_default=True,
        ),
    ]
