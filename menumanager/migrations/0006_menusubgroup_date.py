# Generated by Django 3.2.9 on 2021-11-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menumanager', '0005_auto_20211109_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='menusubgroup',
            name='date',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]