# Generated by Django 4.2.1 on 2023-05-07 23:35

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('control_usuarios', '0002_alter_etiqueta_nombre_alter_user_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apellido',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='nombre',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')]),
        ),
    ]
