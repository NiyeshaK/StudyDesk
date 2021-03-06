# Generated by Django 4.0.1 on 2022-03-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashmin', '0011_remove_noteforms_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteForm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(choices=[('DS', 'DS'), ('DBMS', 'DBMS'), ('OS', 'OS'), ('COA', 'COA'), ('CN', 'CN'), ('DF', 'DF'), ('SE', 'SE'), ('C', 'C'), ('JAVA', 'JAVA'), ('PHP', 'PHP'), ('PYTHON', 'PYTHON')], max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('note', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='file')),
            ],
            options={
                'verbose_name': 'NoteForms',
                'verbose_name_plural': 'NoteForms',
            },
        ),
        migrations.DeleteModel(
            name='NoteForms',
        ),
    ]
