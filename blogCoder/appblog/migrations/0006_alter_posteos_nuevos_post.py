# Generated by Django 4.0.3 on 2022-04-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0005_alter_posteos_nuevos_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteos_nuevos',
            name='post',
            field=models.TextField(),
        ),
    ]
