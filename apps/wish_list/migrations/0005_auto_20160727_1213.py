# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list', '0004_auto_20160727_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='coowners',
            field=models.ManyToManyField(related_name='coowners', to='users.User'),
        ),
        migrations.AlterField(
            model_name='item',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='users.User'),
        ),
    ]