from cProfile import label
from random import choices
from django import forms
from . models import NoteForm, VideoForm
from django.contrib.auth.models import User


note_choice=[
    ('PDF','PDF'),
    ('Handwritten','Handwritten')
]


video_choice=[
    ('Video','Video'),
    ('videoLink','VideoLink')
]

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

des=(
    ('Teacher','Teacher'),
    ('Student','Student')
)

area=(
    ('Core Subject','Core Subject'),
    ('Language Specific','Language Specific')
)

class NotesForms(forms.ModelForm):
    note=forms.ChoiceField(choices=note_choice,widget=forms.RadioSelect)
    subject=forms.ChoiceField(choices=sub)
    class Meta:
        model=NoteForm
        fields=['subject','title','description','note','file']
        labels={'subject':'Subject','title':'Title','description':'Description','note':'Note','file':'File'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            
        }

class VideosForms(forms.ModelForm):
    
    video=forms.ChoiceField(choices=video_choice,widget=forms.RadioSelect)
    subject=forms.ChoiceField(choices=sub)
    class Meta:
        model=VideoForm
        fields=['subject','title','description','video','file','link1']
        labels={'subject':'Subject','title':'Title','description':'Description','video': 'Video','link1':' Video Link','file':'File'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'link1':forms.URLInput(attrs={'class':'form-control'},)
            
        }

# class UserUpdateForm(forms.ModelForm):
#     Designation=forms.ChoiceField(choices=des)
#     subjectArea=forms.ChoiceField(choices=area)
#     class Meta:
#         model=editProfiles
#         fields=['user','email','designation','subarea','Profile','pic']
#         labels={'user':'Name','email':'Email','designation':'Designation','Subarea':'SubjectArea','Profile':'Profile','Pic':'Pic'}
#         widgets={
#             'Profile':forms.TextInput(attrs={'class':'form-control'}),
            
            
#         }

