# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('duration', models.IntegerField(max_length=3)),
                ('intensity', models.IntegerField(max_length=2)),
                ('fitons', models.IntegerField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=51)),
                ('exertion', models.IntegerField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FitUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gcm', models.CharField(default=None, max_length=512, null=True)),
                ('uuid', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=51)),
                ('height', models.IntegerField(max_length=4)),
                ('age', models.IntegerField(max_length=3)),
                ('weight', models.IntegerField(max_length=3)),
                ('diseases', models.CharField(max_length=1024)),
                ('bodytype', models.IntegerField(choices=[(0, b'Slim'), (1, b'Fit'), (2, b'Plum'), (3, b'Obese')])),
                ('fitons', models.IntegerField(max_length=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=51)),
                ('perCatFitons', models.CharField(max_length=51)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=51)),
                ('user', models.ForeignKey(to='profit.FitUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SessionActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('duration', models.IntegerField(max_length=4)),
                ('session', models.ForeignKey(to='profit.Session')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubCat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=51)),
                ('exertion', models.IntegerField(max_length=2)),
                ('cat', models.ForeignKey(to='profit.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('duration', models.IntegerField(max_length=3)),
                ('intensity', models.IntegerField(max_length=2)),
                ('goal', models.ForeignKey(to='profit.Goal')),
                ('subcat', models.ForeignKey(to='profit.SubCat')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeightLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=12)),
                ('weight', models.IntegerField(max_length=3)),
                ('user', models.ForeignKey(to='profit.FitUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sessionactivity',
            name='subcat',
            field=models.ForeignKey(to='profit.SubCat'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='subcat',
            field=models.ForeignKey(to='profit.SubCat'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(to='profit.FitUser'),
            preserve_default=True,
        ),
    ]
