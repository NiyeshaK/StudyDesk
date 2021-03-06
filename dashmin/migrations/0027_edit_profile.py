# Generated by Django 4.0.1 on 2022-04-02 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashmin', '0026_alter_videoform_description_alter_videoform_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='edit_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('Designation', models.CharField(max_length=20)),
                ('subArea', models.CharField(max_length=20)),
                ('profile', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='profilepics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
