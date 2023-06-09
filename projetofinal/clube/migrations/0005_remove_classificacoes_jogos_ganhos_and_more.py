# Generated by Django 4.1.7 on 2023-05-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clube', '0004_alter_classificacoes_jogos_disputados_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classificacoes',
            name='jogos_ganhos',
        ),
        migrations.RemoveField(
            model_name='classificacoes',
            name='jogos_perdidos',
        ),
        migrations.RemoveField(
            model_name='equipa',
            name='escalao',
        ),
        migrations.AlterField(
            model_name='classificacoes',
            name='escalao',
            field=models.CharField(choices=[('Infantis', 'Infantis'), ('Iniciados', 'Iniciados'), ('Cadetes', 'Cadetes')], max_length=20),
        ),
        migrations.AlterField(
            model_name='classificacoes',
            name='jogos_disputados',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='classificacoes',
            name='pontos',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
