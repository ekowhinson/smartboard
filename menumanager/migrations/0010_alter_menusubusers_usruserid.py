# Generated by Django 3.2.9 on 2021-11-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menumanager', '0009_auto_20211113_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menusubusers',
            name='usruserid',
            field=models.CharField(max_length=50),
        ),
    ]