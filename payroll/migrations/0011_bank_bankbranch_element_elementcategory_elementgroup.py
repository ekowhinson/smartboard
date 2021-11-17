# Generated by Django 3.2.9 on 2021-11-16 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0010_auto_20211116_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=150)),
                ('short_name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BankBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=150)),
                ('bankCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.bank')),
            ],
        ),
        migrations.CreateModel(
            name='ElementCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('apply_affordability', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ElementGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=150)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('category', models.CharField(max_length=50)),
                ('acc_no', models.CharField(max_length=80)),
                ('status', models.BooleanField(default=False)),
                ('elementcreated', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('bank_branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='payroll.bankbranch')),
                ('bank_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='payroll.bank')),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('clgcode', models.CharField(max_length=50)),
                ('catcode', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('real', models.CharField(max_length=50)),
                ('typeid', models.CharField(max_length=50)),
                ('emap', models.CharField(max_length=50)),
                ('companyid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='payroll.company')),
            ],
        ),
    ]