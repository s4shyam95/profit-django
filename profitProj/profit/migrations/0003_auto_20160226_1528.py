# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profit', '0002_auto_20160226_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fituser',
            name='name',
            field=models.CharField(default=b'', max_length=51),
        ),
    ]
