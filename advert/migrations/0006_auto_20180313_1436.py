# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-13 09:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0005_postadd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='district',
        ),
        migrations.RemoveField(
            model_name='district',
            name='state',
        ),
        migrations.RemoveField(
            model_name='postadd',
            name='category',
        ),
        migrations.RemoveField(
            model_name='postadd',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='postadd',
            name='sub_category',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='PostAdd',
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
