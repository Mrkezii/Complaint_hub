# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-24 15:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0002_auto_20160524_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academiccomplaint',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 15, 36, 56, 732739, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='exeat',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 15, 36, 56, 734065, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ppd',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 15, 36, 56, 736575, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='specialadmrequest',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 15, 36, 56, 737380, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='workstudy',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 24, 15, 36, 56, 735572, tzinfo=utc)),
        ),
    ]
