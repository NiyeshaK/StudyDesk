# Generated by Django 4.0.1 on 2022-03-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashmin', '0016_note2_delete_note1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note3',
            fields=[
                ('name', models.CharField(max_length=10)),
                ('add', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='file')),
            ],
        ),
        migrations.DeleteModel(
            name='Note2',
        ),
    ]
