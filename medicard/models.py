from django.db import models    #importar librerias de modelos.
from django.utils import timezone  #Importar libreria de zona horaria.
from django.contrib.auth.models import User  #Importar desde los modelos autorizados por Django la base de datos de User.
from django.db.models.signals import post_save  #Importar desde las señales de los modelos la señal post-save
from django.dispatch import receiver  #Importar del despacho de señales de Django la señal receiver.
#BD = Base de datos.
class Medicard_rd(models.Model): #class es una palabra clave que indica que estamos definiendo un objeto. Medicard_rd es el nombre del modelo. models.Models significa que es un modelo de Django, asi Django sabe que debe almacenarlo en la BD.
    Titulo = models.CharField(max_length=40, default='')  #Titulo es un campo tipo CHAR con una capacidad-max de 40 caract.
    hospital = models.CharField(max_length=30, default='') #hospital es un campo tipo char con una capacidad-max de 30 caract.
    area = models.CharField(max_length=30)  #area es un campo tipo char con una capacidad-max de 30 caract. el default es la referencia de la base de datos.
    paciente = models.ForeignKey('auth.User', related_name= 'paciente', default = '') #paciente es una llave foranea en la base de datos con la tabla de auth.User.
    doctor = models.ForeignKey('auth.User', related_name= 'doctor', default='') #doctor es una llave foranea con la tabla de auth.User.
    reporte = models.TextField() #reporte es un campo de texto.
    fecha_creacion = models.DateTimeField(default=timezone.now) #fecha_creacion es un campo de tiempo y fecha, el fefault viene dado por la libreria timezone.now, que otorga el tiempo y fecha de la zona horaria.
    Telefono = models.CharField(max_length=10, default='') #Telefono es un campo con capacidad-max de 10 caract.
    Imagen = models.FileField(upload_to='%Y/%m/%d', blank = True, default='') #Imagen es un campo de archivo, este carga el archivo a la carpeta seleccionada en setting.py con MEDIA_ROOT almacenandolo en una carpeta por fecha de subida.


    def publish(self): #def significa que es una funcion o metodo, publish es el nombre del metodo. self indica que es un atributo de la instancia.
        self.fecha_creacion = timezone.now() #Esto indica que en la funcion pusblish regrese fecha_creacion
        self.save() #Esto indica que en la funcion publish regrese la funcion propia de Django save().

    def __str__(self): #Esta es la funcion propia de Django __str__
        return self.Titulo + " " + " " + self.paciente.username + " " + " " + self.doctor.username
#Esta funcion retorna el titulo, el username del paciente y el username del doctor como un string de texto hacia el Django-admin.
class perfil(models.Model): #Este es otro modelo llamado Perfil
    Medico_autorizado = 1 #Este es el rol medicoa_autorizado
    PACIENTE = 2 #Este es el rol Paciente
    ROLES = ( #Esto indica a Django que medic_autorizado y paciente son roles
        ( Medico_autorizado, 'Medico autorizado'),
        (PACIENTE, 'Paciente'),
    ) #blank = True le dice a la base de datos y a Django que se puede dejar en blanco este campo.
    user = models.OneToOneField(User, on_delete=models.CASCADE) #user tiene una relacion uno a uno con el Usuario, on_delete =models.CASCADE quiere decir que al momento que se elminine ese usuario se elimine el perfil en CASCada.
    Direccion = models.CharField(max_length=80, blank = True) #Direccion es un campo tipo char con una capacidad-max de 80 caract.
    rol = models.PositiveSmallIntegerField(choices=ROLES, null = True, blank=True) #rol es un campo de enteros donde las opciones son los ROLES definidos anteriormente.
    Tipo_de_sangre = models.CharField(max_length=3, default='') #Tipo_de_sangre es un campo tipo Char, con una capacidad max de 3 caract.
    Sexo = models.CharField(max_length=9, default='') #Sexo es un campo tipo char con una capacidad maxima de 9 caracteres.
    Fecha_nacimiento = models.CharField(max_length=10, default='')
    ARS = models.CharField(max_length=10, default='')
    Plan_ARS = models.CharField(max_length=10, default='')
    Patologia = models.TextField(blank = True, default='')
    Medicacion_frecuente = models.CharField(max_length=30, blank = True, default='')
    Alergias = models.TextField(blank = True, default='')
    Centro_medico_frecuente = models.CharField(max_length=40, blank = True, default='')
    Dr_cabecera = models.CharField(max_length=30, blank = True, default='')
    numero_Dr_cabecera = models.IntegerField(blank = True, default='0')
    Familiar_cercano = models.CharField(max_length=30, blank = True, default='')
    Numero_familiar_cercano = models.IntegerField(blank = True, default='0')
    Ultima_intervencion_quirurgica = models.CharField(max_length=50, blank = True, default='')
    Intervenciones_quirurgicas = models.TextField(blank = True, default='')
    Cedula = models.IntegerField(default='0')

    @receiver(post_save, sender=User) #@receiver es una señal de Django que contiene a post_save y  utilizando el metodo sender propio de Django lo asocia al User.
    def create_or_update_user_profile(sender, instance, created, **kwargs): #Este es la definicion del metodo llamada create_or_update_user_profile
        if created: #es una condicional tipica de Python.
            perfil.objects.create(user=instance)
        instance.perfil.save()
#Esta condicionante nos dice que si el perfil ya ha sido creado se actulice medicante la instancia
    def __str__(self):
        return self.user.username
# Create your models here.
