# Generated by Django 4.0.1 on 2022-04-05 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashmin', '0028_rename_edit_profile_edit_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='edit_user',
        ),
    ]
