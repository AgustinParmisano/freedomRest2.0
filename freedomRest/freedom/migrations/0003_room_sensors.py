# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freedom', '0002_auto_20150812_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='sensors',
            field=models.ForeignKey(related_name='rooms', to='freedom.Sensor', null=b'True'),
        ),
    ]
