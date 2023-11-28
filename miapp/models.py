from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

tipohito = [('V','Vacaciones'),('F','Feriado'),('SA','Suspension de Actividades'),
                                      ('SaPM','Suspension de Actividades PM'),('P','Periodo Lectivo'),('S','Suspension de Evaluaciones'),
                                      ('C', 'Ceremonia'),('Ed', 'EDDA'),('E', 'Evaluacion'),
                                      ('A', 'Ayudantias'),('H', 'Hito Academico'),('Se', 'Secretaria Academica'),
                                      ('O', 'OAI')]
tiposegmento = [('Co','Comunidad usm'),('Es', 'Estudiante'),('Pr', 'Profesor'),('Je','Jefe de Carrera')]

class Hito(models.Model):
    fecha_inicio = models.DateTimeField(null= True, blank=True)
    fecha_termino = models.DateTimeField(null= True, blank=True)
    todo_el_dia = models.BooleanField(default=False)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50,
                            choices=[('V','Vacaciones'),('F','Feriado'),('SA','Suspension de Actividades'),
                                    ('SaPM','Suspension de Actividades PM'),('P','Periodo Lectivo'),('S','Suspension de Evaluaciones'),
                                    ('C', 'Ceremonia'),('Ed', 'EDDA'),('E', 'Evaluacion'),
                                    ('A', 'Ayudantias'),('H', 'Hito Academico'),('Se', 'Secretaria Academica'),
                                    ('O', 'OAI')], null=True, blank=True)
    segmento = models.CharField(max_length=50, choices=[('Co','Comunidad usm'),('Es', 'Estudiante'),('Pr', 'Profesor'),('Je','Jefe de Carrera')], default='Co')
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class UserRol(models.Model):
    Tipo_Rol = [('Co','Comunidad usm'),('Es', 'Estudiante'),('Pr', 'Profesor'),('Je','Jefe de Carrera'),('De','Developer')]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userrol')
    rol = models.CharField(max_length=25,choices=Tipo_Rol,default='Co')

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['id']

    def __str__(self):
        return self.user.username + "/" + self.get_rol_display()

def create_UserRol(sender, instance, created, **kwargs):
    if created:
        UserRol.objects.create(user=instance)
    
def save_UserRol(sender, instance, **kwargs):
    instance.userrol.save()

post_save.connect(create_UserRol, sender=User)
post_save.connect(save_UserRol, sender=User)
