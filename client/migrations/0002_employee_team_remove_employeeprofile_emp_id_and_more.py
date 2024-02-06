# Generated by Django 5.0.1 on 2024-01-25 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='employeeprofile',
            name='emp_id',
        ),
        migrations.RemoveField(
            model_name='employeeprofile',
            name='team_id',
        ),
        migrations.RemoveField(
            model_name='employeeprofile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='employeeprofile',
            name='profile_id',
        ),
        migrations.AddField(
            model_name='employeeprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='employeeprofile',
            table=None,
        ),
        migrations.AddField(
            model_name='employeeprofile',
            name='employee',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='client.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeeprofile',
            name='team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='client.team'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Teams',
        ),
    ]