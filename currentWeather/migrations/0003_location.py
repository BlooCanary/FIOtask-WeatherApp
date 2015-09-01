# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currentWeather', '0002_delete_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('zipCode', models.CharField(max_length=5)),
                ('temperature', models.CharField(max_length=5)),
                ('condition', models.CharField(max_length=10)),
            ],
        ),
    ]
