# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freedom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='owner',
        ),
        migrations.AlterField(
            model_name='sensor',
            name='room',
            field=models.ForeignKey(to='freedom.Room'),
        ),
    ]
