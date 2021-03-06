# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateField()),
                ('followers', models.ManyToManyField(related_name='followers', to='users.User')),
                ('list_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_owner', to='users.User')),
            ],
        ),
    ]
