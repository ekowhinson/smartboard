# Generated by Django 3.2.9 on 2021-11-29 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0014_auto_20211128_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]