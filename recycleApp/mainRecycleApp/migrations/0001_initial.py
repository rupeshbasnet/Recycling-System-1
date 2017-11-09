# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 03:33
'''Initial Migrations for mainRecycleApp'''
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    '''Migrations class'''
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecyclingCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, 
                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('borough', models.TextField()),
                ('state', models.TextField()),
                ('zipcode', models.TextField()),
                ('phone', models.TextField()),
                ('picks_up', models.TextField()),
                ('recycleType', models.TextField()),
                ('website', models.TextField()),
            ],
        ),
    ]
