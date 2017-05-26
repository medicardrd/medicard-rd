# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('medicard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicard_rd',
            name='doctor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default='', related_name='doctor'),
        ),
        migrations.AlterField(
            model_name='medicard_rd',
            name='paciente',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default='', related_name='paciente'),
        ),
    ]
