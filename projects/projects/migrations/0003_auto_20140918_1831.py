# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField(verbose_name='link')),
                ('layer', models.ForeignKey(verbose_name='layer', to='projects.Layer')),
                ('status', models.ForeignKey(verbose_name='status', to='projects.Status')),
                ('version', models.ForeignKey(verbose_name='version', to='projects.Version')),
            ],
            options={
                'ordering': ('-version__tag',),
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='layerversion',
            name='layer',
        ),
        migrations.RemoveField(
            model_name='layerversion',
            name='status',
        ),
        migrations.RemoveField(
            model_name='layerversion',
            name='version',
        ),
        migrations.DeleteModel(
            name='LayerVersion',
        ),
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ('-tag',), 'verbose_name': 'version', 'verbose_name_plural': 'versions'},
        ),
        migrations.AlterField(
            model_name='component',
            name='project',
            field=models.ForeignKey(related_name=b'components', verbose_name='project', to='projects.Project'),
        ),
        migrations.AlterUniqueTogether(
            name='version',
            unique_together=set([('component', 'tag')]),
        ),
    ]
