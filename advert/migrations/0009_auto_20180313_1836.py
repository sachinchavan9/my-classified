# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-13 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0008_postadd_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='postadd',
            name='subcategory',
        ),
        migrations.AlterField(
            model_name='postadd',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category_p', to='advert.Category'),
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
