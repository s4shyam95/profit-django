# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profit', '0003_auto_20160226_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='exertion',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='age',
            field=models.IntegerField(default=None, max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='bodytype',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(0, b'Slim'), (1, b'Fit'), (2, b'Plum'), (3, b'Obese')]),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='diseases',
            field=models.CharField(default=None, max_length=1024, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='fitons',
            field=models.IntegerField(default=None, max_length=7, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='gcm',
            field=models.CharField(default=None, max_length=512, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='height',
            field=models.IntegerField(default=None, max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fituser',
            name='weight',
            field=models.IntegerField(default=None, max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='subcat',
            name='exertion',
            field=models.IntegerField(max_length=5),
        ),
    ]
