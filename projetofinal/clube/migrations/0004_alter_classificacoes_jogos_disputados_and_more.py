# Generated by Django 4.1.7 on 2023-05-08 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clube', '0003_equipa_rename_escalão_treinador_equipa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificacoes',
            name='jogos_disputados',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='classificacoes',
            name='jogos_ganhos',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='classificacoes',
            name='jogos_perdidos',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='classificacoes',
            name='pontos',
            field=models.IntegerField(default=1),
        ),
    ]
