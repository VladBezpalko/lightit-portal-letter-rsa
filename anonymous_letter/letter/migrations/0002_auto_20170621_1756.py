# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letter',
            old_name='response',
            new_name='answer',
        ),
        migrations.AddField(
            model_name='letter',
            name='codeword',
            field=models.SlugField(unique=True),
            preserve_default=False,
        ),
    ]
