# Generated by Django 4.0.1 on 2022-04-07 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashmin', '0033_alter_editprofiles_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editprofiles',
            options={'verbose_name': 'Edit Profiles', 'verbose_name_plural': 'Edit Profiles'},
        ),
        migrations.RenameField(
            model_name='editprofiles',
            old_name='user',
            new_name='user_name',
        ),
    ]