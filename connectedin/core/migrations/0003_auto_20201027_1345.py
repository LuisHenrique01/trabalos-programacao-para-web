# Generated by Django 3.1 on 2020-10-27 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_convite'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='data_nascimento',
            field=models.DateField(default='2020-01-01', verbose_name='Data nascimento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
