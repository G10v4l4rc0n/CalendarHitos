from django.db import models


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
