# Generated by Django 5.2.1 on 2025-05-20 04:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses_name', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Age', models.TextField(blank=True, max_length=255, null=True)),
                ('Phone_number', models.TextField(blank=True, max_length=255, null=True)),
                ('College_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.college')),
                ('courses_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.courses')),
            ],
        ),
    ]
