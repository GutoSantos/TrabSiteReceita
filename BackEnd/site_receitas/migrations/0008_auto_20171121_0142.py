# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 03:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_receitas', '0007_auto_20171119_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='fk_receita_imagem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='site_receitas.Receita'),
        ),
    ]