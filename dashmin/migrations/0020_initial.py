# Generated by Django 4.0.1 on 2022-03-08 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashmin', '0019_delete_note3'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotesForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files')),
            ],
            options={
                'verbose_name': 'NotesForm',
                'verbose_name_plural': 'NotesForm',
            },
        ),
    ]
