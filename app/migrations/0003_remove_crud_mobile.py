# Generated by Django 4.2.7 on 2024-02-24 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_crud_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crud',
            name='mobile',
        ),
    ]
