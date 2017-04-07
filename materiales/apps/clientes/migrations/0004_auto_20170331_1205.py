# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20170331_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default=1, max_length=10),
        ),
    ]