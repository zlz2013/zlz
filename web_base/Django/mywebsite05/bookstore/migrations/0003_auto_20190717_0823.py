# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-17 08:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_remove_book_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, unique=True, verbose_name='作者名')),
                ('age', models.IntegerField(default=1, verbose_name='年龄')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='邮箱')),
            ],
        ),
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='作者名')),
                ('age', models.IntegerField(default=1, verbose_name='年龄')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='邮箱')),
                ('author', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookstore.Author')),
            ],
        ),
        migrations.RenameField(
            model_name='book',
            old_name='pub_house',
            new_name='pub',
        ),
    ]