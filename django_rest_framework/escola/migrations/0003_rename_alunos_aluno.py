# Generated by Django 5.0.6 on 2024-06-15 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_alter_curso_nivel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alunos',
            new_name='Aluno',
        ),
    ]