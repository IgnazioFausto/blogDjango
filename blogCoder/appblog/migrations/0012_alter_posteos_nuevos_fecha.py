# Generated by Django 4.0.3 on 2022-04-19 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0011_alter_posteos_nuevos_fecha_alter_posteos_nuevos_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteos_nuevos',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
