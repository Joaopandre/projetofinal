# Generated by Django 4.1.7 on 2023-05-09 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clube', '0017_alter_atleta_equipa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atleta',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
