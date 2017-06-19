# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('medicard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='ARS',
            field=models.CharField(max_length=10, default=''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='Alergias',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='Centro_medico_frecuente',
            field=models.CharField(max_length=40, default=''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='Dr_cabecera',
            field=models.CharField(max_length=30, default=''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='Familiar_cercano',
            field=models.CharField(max_length=30, default=''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='Fecha_nacimiento',
            field=models.CharField(max_length=10, default=''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='Medicacion_frecuente',
            field=models.CharField(max_length=30, default=''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='Patologia',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='Plan_ARS',
            field=models.CharField(max_length=10, default=''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='Sexo',
            field=models.CharField(max_length=9, default=''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='Tipo_de_sangre',
            field=models.CharField(max_length=3, default=''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='numero_Dr_cabecera',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='medicard_rd',
            name='doctor',
            field=models.ForeignKey(default='', related_name='doctor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='medicard_rd',
            name='paciente',
            field=models.ForeignKey(default='', related_name='paciente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='Direccion',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
