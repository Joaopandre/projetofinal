# Generated by Django 4.1.7 on 2023-05-09 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clube', '0020_alter_atleta_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voto_Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('vai_ao_jogo', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='jogo',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='hora',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='local',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Votacao_jogo',
        ),
        migrations.AddField(
            model_name='voto_jogo',
            name='jogo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clube.jogo'),
        ),
        migrations.AddField(
            model_name='voto_jogo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]