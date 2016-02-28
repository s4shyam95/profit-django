# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fituser',
            name='age',
            field=models.IntegerField(default=None, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='bodytype',
            field=models.IntegerField(default=None, null=True, choices=[(0, b'Slim'), (1, b'Fit'), (2, b'Plum'), (3, b'Obese')]),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='diseases',
            field=models.CharField(default=None, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='fitons',
            field=models.IntegerField(default=None, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='height',
            field=models.IntegerField(default=None, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='name',
            field=models.CharField(default=None, max_length=51, null=True),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='weight',
            field=models.IntegerField(default=None, max_length=3, null=True),
        ),
    ]
