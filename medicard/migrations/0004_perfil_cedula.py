# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicard', '0003_auto_20170615_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='Cedula',
            field=models.IntegerField(default='0'),
        ),
    ]
