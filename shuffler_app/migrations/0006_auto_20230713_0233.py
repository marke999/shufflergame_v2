# Generated by Django 3.2.20 on 2023-07-13 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shuffler_app', '0005_alter_user_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Username',
            new_name='username',
        ),
    ]