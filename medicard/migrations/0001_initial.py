# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicard_rd',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Titulo', models.CharField(default='', max_length=40)),
                ('hospital', models.CharField(default='', max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('doctor', models.CharField(default='', max_length=20)),
                ('reporte', models.TextField()),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('Telefono', models.CharField(default='', max_length=10)),
                ('Imagen', models.FileField(default='', blank=True, upload_to='%Y/%m/%d')),
                ('paciente', models.ForeignKey(default='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Direccion', models.CharField(blank=True, max_length=40)),
                ('rol', models.PositiveSmallIntegerField(null=True, choices=[(1, 'Medico autorizado'), (2, 'Paciente')], blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
