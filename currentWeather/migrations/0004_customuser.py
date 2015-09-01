# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currentWeather', '0003_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='customUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(max_length=20)),
            ],
        ),
    ]
