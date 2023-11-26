# Generated by Django 4.1.5 on 2023-11-26 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0004_alter_hito_fecha_inicio_alter_hito_fecha_termino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hito',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hito',
            name='fecha_termino',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hito',
            name='tipo',
            field=models.CharField(blank=True, choices=[('V', 'Vacaciones'), ('F', 'Feriado'), ('SA', 'Suspension de Actividades'), ('SaPM', 'Suspension de Actividades PM'), ('P', 'Periodo Lectivo'), ('S', 'Suspension de Evaluaciones'), ('C', 'Ceremonia'), ('Ed', 'EDDA'), ('E', 'Evaluacion'), ('A', 'Ayudantias'), ('H', 'Hito Academico'), ('Se', 'Secretaria Academica'), ('O', 'OAI')], max_length=50, null=True),
        ),
    ]