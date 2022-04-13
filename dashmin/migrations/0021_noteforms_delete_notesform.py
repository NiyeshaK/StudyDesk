# Generated by Django 4.0.1 on 2022-03-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashmin', '0020_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteForms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('DS', 'DS'), ('OS', 'OS'), ('DBMS', 'DBMS'), ('COA', 'COA'), ('DF', 'DF'), ('CN', 'CN'), ('C', 'C'), ('JAVA', 'JAVA'), ('PHP', 'PHP'), ('PYTHON', 'PYTHON')], max_length=20)),
                ('title', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('note', models.CharField(max_length=10)),
                ('file', models.FileField(upload_to='files')),
            ],
            options={
                'verbose_name': 'NotesForm',
                'verbose_name_plural': 'NotesForm',
            },
        ),
        migrations.DeleteModel(
            name='NotesForm',
        ),
    ]
