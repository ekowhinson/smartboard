# Generated by Django 3.2.9 on 2021-11-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0011_bank_bankbranch_element_elementcategory_elementgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_active',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_verify',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_ip',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='password_reset_code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='token',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]