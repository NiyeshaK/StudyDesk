from tabnanny import verbose
from tkinter import CASCADE

from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from django.dispatch import receiver
sub=(
    ('DS','DS'),
    ('OS','OS'),
    ('DBMS','DBMS'),
    ('COA','COA'),
    ('DF','DF'),
    ('CN','CN'),
    ('C','C'),
    ('JAVA','JAVA'),
    ('PHP','PHP'),
    ('PYTHON','PYTHON')
)


class NoteForm(models.Model):
    subject=models.CharField(choices=sub,max_length=20)
    title=models.CharField(max_length=10)
    description=models.TextField(max_length=200)
    date=models.DateField(auto_now_add=True)
    note=models.CharField(max_length=10)
    file=models.FileField(upload_to='files')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "NoteForm"
        verbose_name_plural = "NoteForm"

class VideoForm(models.Model):
    subject=models.CharField(choices=sub,max_length=20)
    title=models.CharField(max_length=10)
    description=models.CharField(max_length=300)
    date=models.DateField(auto_now_add=True)
    video=models.CharField(max_length=10)
    file=models.FileField(upload_to='videos',null=True,default=None,blank=True)
    link1=models.URLField(max_length=300,null=True,default=None,blank=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "VideoForm"
        verbose_name_plural = "VideoForm"

# class edit_userProfile(models.Model):
#     user_name=models.CharField(max_length=20)
#     email=models.CharField(max_length=20)
#     designation=models.CharField(max_length=20)
#     subarea=models.CharField(max_length=20)
#     Profile=models.CharField(max_length=300)
#     pic=models.ImageField(upload_to='pics',null=True,default=None,blank=True)
    

#     def __str__(self):
#         return self.user.username

#     class Meta:
#         verbose_name = "Edit Profile"
#         verbose_name_plural = "Edit Profile"

class user_edit(models.Model):
    user_name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    subarea=models.CharField(max_length=20)
    Profile=models.CharField(max_length=300)
    pic=models.ImageField(upload_to='pics',null=True,default=None,blank=True)
    

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "user_edit"
        verbose_name_plural = "user_edit"