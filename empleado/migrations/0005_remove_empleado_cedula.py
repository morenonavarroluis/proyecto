# Generated by Django 4.2.9 on 2025-07-16 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0004_rename_cdula_empleado_cedula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='cedula',
        ),
    ]
