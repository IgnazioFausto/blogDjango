# Generated by Django 4.0.3 on 2022-04-29 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0009_alter_mensajes_destinatario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='destinatario',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
