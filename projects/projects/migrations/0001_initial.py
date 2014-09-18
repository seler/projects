# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='order')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'component',
                'verbose_name_plural': 'components',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'files', verbose_name='file')),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='order')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'layer',
                'verbose_name_plural': 'layers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LayerVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField(verbose_name='link')),
                ('layer', models.ForeignKey(verbose_name='layer', to='projects.Layer')),
            ],
            options={
                'ordering': ('-version__tag',),
                'verbose_name': 'layer version',
                'verbose_name_plural': 'layer versions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='order')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'status',
                'verbose_name_plural': 'statuses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(default=b'v0.1', max_length=255, verbose_name='tag')),
                ('component', models.ForeignKey(verbose_name='component', to='projects.Component')),
            ],
            options={
                'ordering': ('-tag',),
                'get_latest_by': '',
                'verbose_name': 'version',
                'verbose_name_plural': 'versions',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='layerversion',
            name='status',
            field=models.ForeignKey(verbose_name='status', to='projects.Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='layerversion',
            name='version',
            field=models.ForeignKey(verbose_name='version', to='projects.Version'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='component',
            name='project',
            field=models.ForeignKey(verbose_name='project', to='projects.Project'),
            preserve_default=True,
        ),
    ]
