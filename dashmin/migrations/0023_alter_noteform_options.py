# Generated by Django 4.0.1 on 2022-03-09 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashmin', '0022_rename_noteforms_noteform'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noteform',
            options={'verbose_name': 'NoteForm', 'verbose_name_plural': 'NoteForm'},
        ),
    ]
