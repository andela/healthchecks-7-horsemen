# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-02 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20171027_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='nag_status_on',
            field=models.BooleanField(default=False),
        ),
    ]