# Generated by Django 3.1.4 on 2020-12-28 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signupApp', '0002_auto_20201228_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='username',
            new_name='name',
        ),
    ]