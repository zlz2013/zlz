# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-16 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_auto_20190715_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(verbose_name='出版时间'),
        ),
    ]
