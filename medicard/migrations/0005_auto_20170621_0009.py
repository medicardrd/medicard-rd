# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicard', '0004_perfil_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='Alergias',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='Centro_medico_frecuente',
            field=models.CharField(default='', blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='Dr_cabecera',
            field=models.CharField(default='', blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='Familiar_cercano',
            field=models.CharField(default='', blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='Intervenciones_quirurgicas',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='Medicacion_frecuente',
            field=models.CharField(default='', blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='Numero_familiar_cercano',
            field=models.IntegerField(default='0', blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='Patologia',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='Ultima_intervencion_quirurgica',
            field=models.CharField(default='', blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='numero_Dr_cabecera',
            field=models.IntegerField(default='0', blank=True),
        ),
    ]
