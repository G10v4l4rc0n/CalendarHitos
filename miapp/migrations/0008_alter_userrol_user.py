# Generated by Django 4.2 on 2023-11-28 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('miapp', '0007_userrol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrol',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userrol', to=settings.AUTH_USER_MODEL),
        ),
    ]