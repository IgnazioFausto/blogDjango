# Generated by Django 4.0.3 on 2022-04-28 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfiles', '0005_mensajes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensajes',
            old_name='usuario',
            new_name='emisor',
        ),
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinatario', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emisor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
