# Generated by Django 5.1 on 2024-11-09 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birdchat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='autor',
            new_name='Autor',
        ),
    ]
