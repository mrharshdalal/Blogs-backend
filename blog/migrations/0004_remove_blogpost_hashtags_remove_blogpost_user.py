# Generated by Django 4.2.5 on 2023-09-17 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='hashtags',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='user',
        ),
    ]
