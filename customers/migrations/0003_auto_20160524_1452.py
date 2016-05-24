# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20160523_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='odcustomer',
            options={'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterField(
            model_name='odcustomer',
            name='phone',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='odcustomer',
            name='picture',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]