# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-15 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_book_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='作者名')),
                ('age', models.IntegerField(verbose_name='年龄')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='pub_date',
            field=models.DateField(auto_now=True, verbose_name='出版时间'),
        ),
    ]