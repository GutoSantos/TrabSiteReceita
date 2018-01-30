# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_receitas', '0006_auto_20171119_1313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receita',
            options={'ordering': ['dataCadastro', '-nome_receita', 'rating']},
        ),
        migrations.AddField(
            model_name='receita',
            name='dataCadastro',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='receita',
            name='num_votos',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='receita',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]