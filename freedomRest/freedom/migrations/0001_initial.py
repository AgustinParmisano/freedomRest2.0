# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('roomName', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(related_name='rooms', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sensorName', models.CharField(max_length=100)),
                ('room', models.ForeignKey(related_name='sensors', to='freedom.Room')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='sensor',
            unique_together=set([('sensorName', 'room')]),
        ),
    ]
