# Generated by Django 4.0.4 on 2022-12-21 14:53

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_story_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(null=True, upload_to='files/')),
            ],
        ),
        migrations.AlterModelManagers(
            name='story',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='story',
            name='classif',
            field=models.CharField(max_length=150, verbose_name='Категория'),
        ),
    ]
