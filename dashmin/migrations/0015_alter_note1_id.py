# Generated by Django 4.0.1 on 2022-03-08 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashmin', '0014_rename_ex_note1_delete_noteform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note1',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]