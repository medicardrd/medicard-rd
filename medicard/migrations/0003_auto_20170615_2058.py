# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicard', '0002_auto_20170615_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='Intervenciones_quirurgicas',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='Numero_familiar_cercano',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='Ultima_intervencion_quirurgica',
            field=models.CharField(max_length=50, default=''),
        ),
    ]
