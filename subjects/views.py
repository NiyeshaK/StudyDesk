import os
from django.http import HttpResponse
from django.shortcuts import render
from asyncio.base_futures import _FINISHED
from pyexpat.errors import messages
from turtle import title
from unittest import result
from django.shortcuts import redirect, render
# from . forms import *
from django.contrib import messages
from django.views import generic
from django.http import HttpResponse
from dashmin.models import *

# Create your views here.
def python(request):
    notedata=NoteForm.objects.filter(subject="python")
    videodata=VideoForm.objects.filter(subject="python")
    # sub="DS"
    return render(request,'temp/subjects.html',{'d1':notedata,'d2':videodata})

def DS(request):
    notedata=NoteForm.objects.filter(subject="DS")
    videodata=VideoForm.objects.filter(subject="DS")
    # sub="DS"
    return render(request,'temp/subjects.html',{'d1':notedata,'d2':videodata})

def OS(request):
    notedata=NoteForm.objects.filter(subject="OS")
    videodata=VideoForm.objects.filter(subject="OS")
    # sub="DS"
    return render(request,'temp/subjects.html',{'d1':notedata,'d2':videodata})

def dbms(request):
    notedata=NoteForm.objects.filter(subject="DBMS")
    videodata=VideoForm.objects.filter(subject="DBMS")
    # sub="DS"
    return render(request,'temp/subjects.html',{'d1':notedata,'d2':videodata})

def df(request):
    notedata=NoteForm.objects.filter(subject="DF")
    videodata=VideoForm.objects.filter(subject="DF")
    # sub="DS"
    return render(request,'temp/subjects.html',{'d1':notedata,'d2':videodata})

def coa(request):
    notedata=NoteForm.objects.filter(subject="COA")
    videodata=VideoForm.objects.filter(subject="COA")
    # sub="DS"
    return render(request,'temp/subjects.html',{'d1':notedata,'d2':videodata})

def cn(request):
    notedata=NoteForm.objects.filter(subject="CN")
    videodata=VideoForm.objects.filter(subject="CN")
    # sub="DS"
    return render(request,'temp/subjects.html',{'d1':notedata,'d2':videodata})

def se(request):
    notedata=NoteForm.objects.filter(subject="SE")
    videodata=VideoForm.objects.filter(subject="SE")
    # sub="DS"
    return render(request,'temp/subjects.html',{'d1':notedata,'d2':videodata})

def c(request):
    notedata=NoteForm.objects.filter(subject="C")
    videodata=VideoForm.objects.filter(subject="C")
    # sub="DS"
    return render(request,'temp/subjects.html',{'d1':notedata,'d2':videodata})

def java(request):
    notedata=NoteForm.objects.filter(subject="JAVA")
    videodata=VideoForm.objects.filter(subject="JAVA")
    # sub="DS"
    return render(request,'temp/subjects.html',{'d1':notedata,'d2':videodata})

def php(request):
    notedata=NoteForm.objects.filter(subject="PHP")
    videodata=VideoForm.objects.filter(subject="PHP")
    # sub="DS"
    return render(request,'temp/subjects.html',{'d1':notedata,'d2':videodata})



def subjects(request):
    return render(request,'temp/courses.html')
    
