# Generated by Django 4.0.1 on 2022-03-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashmin', '0024_videoform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoform',
            name='file',
            field=models.FileField(null=True, upload_to='videos'),
        ),
        migrations.AlterField(
            model_name='videoform',
            name='link1',
            field=models.URLField(max_length=300, null=True),
        ),
    ]
