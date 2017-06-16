# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-16 03:06
from __future__ import unicode_literals

import NPFinal.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NPFinal', '0003_auto_20170603_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=100, validators=[NPFinal.forms.Reg.valid_mail])),
                ('name', models.CharField(max_length=50, validators=[NPFinal.forms.Reg.valid_name])),
                ('password', models.CharField(max_length=50, validators=[NPFinal.forms.Reg.valid_pwd])),
            ],
        ),
    ]
