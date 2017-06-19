from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Medicard_rd(models.Model):
    Titulo = models.CharField(max_length=40, default='')
    hospital = models.CharField(max_length=30, default='')
    area = models.CharField(max_length=30)
    paciente = models.ForeignKey('auth.User', related_name= 'paciente', default = '')
    doctor = models.ForeignKey('auth.User', related_name= 'doctor', default='')
    reporte = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    Telefono = models.CharField(max_length=10, default='')
    Imagen = models.FileField(upload_to='%Y/%m/%d', blank = True, default='')

    def publish(self):
        self.fecha_creacion = timezone.now()
        self.save()

    def __str__(self):
        return self.Titulo + " " + " " + self.paciente.username + " " + " " + self.doctor.username

class perfil(models.Model):
    Medico_autorizado = 1
    PACIENTE = 2
    ROLES = (
        ( Medico_autorizado, 'Medico autorizado'),
        (PACIENTE, 'Paciente'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Direccion = models.CharField(max_length=80, blank = True)
    rol = models.PositiveSmallIntegerField(choices=ROLES, null = True, blank=True)
    Tipo_de_sangre = models.CharField(max_length=3, default='')
    Sexo = models.CharField(max_length=9, default='')
    Fecha_nacimiento = models.CharField(max_length=10, default='')
    ARS = models.CharField(max_length=10, default='')
    Plan_ARS = models.CharField(max_length=10, default='')
    Patologia = models.TextField(default='')
    Medicacion_frecuente = models.CharField(max_length=30, default='')
    Alergias = models.TextField(default='')
    Centro_medico_frecuente = models.CharField(max_length=40, default='')
    Dr_cabecera = models.CharField(max_length=30, default='')
    numero_Dr_cabecera = models.IntegerField(default='0')
    Familiar_cercano = models.CharField(max_length=30, default='')
    Numero_familiar_cercano = models.IntegerField(default='0')
    Ultima_intervencion_quirurgica = models.CharField(max_length=50, default='')
    Intervenciones_quirurgicas = models.TextField(default='')
    Cedula = models.IntegerField(default='0')

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            perfil.objects.create(user=instance)
        instance.perfil.save()

    def __str__(self):
        return self.user.username
# Create your models here.
