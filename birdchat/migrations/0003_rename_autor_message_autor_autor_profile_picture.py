# Generated by Django 4.2.16 on 2024-11-29 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdchat', '0002_rename_autor_message_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='Autor',
            new_name='autor',
        ),
        migrations.AddField(
            model_name='autor',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
