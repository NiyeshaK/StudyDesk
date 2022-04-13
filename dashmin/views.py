import email
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.views import View
from .forms import *
from .models import *
from django.contrib.auth.models import User


from . import *



# Create your views here.
def profile(request):
    return render(request,'dash/profile.html')

def form(request):
    form1=NotesForms()
    form2=VideosForms()
    context={
        'form1':form1,
        'form2':form2
    }
    return render(request,'dash/form.html',context)

# def form(request):
#     form2=VideoForm()
#     return render(request,'dash/form.html',{'form2':form2})

def submit(request):
    form=NotesForms(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('form')
    else:
        return render(request,'dash/form.html',{'form':form})
    

def table(request):
    data1=NoteForm.objects.all()
    data2=VideoForm.objects.all()
    context={
        'data1':data1,
        'data2':data2
    }
    return render(request,'dash/table.html',context)

def view1(request,pk):
    notedata=NoteForm.objects.get(id=pk)
    return render(request,'dash/data.html',{'d1':notedata})

def view2(request,pk):
    videodata=VideoForm.objects.get(id=pk)
    return render(request,'dash/data.html',{'d2':videodata})

def vid(request):
    form=VideosForms(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('form')
    else:
        return render(request,'dash/form.html',{'form':form})

def delete_n(request,pk=None):
    NoteForm.objects.get(id=pk).delete()
    return redirect("table")

def delete_v(request,pk=None):
    VideoForm.objects.get(id=pk).delete()
    return redirect("table")

def edit(request):
    if request.method=="POST":
        u_name=request.POST.get('u_name')
        u_email=request.POST.get('u_email')
        desg=request.POST.get('desg')
        sub_area=request.POST.get('area')
        profile=request.POST.get('profile')
        pic=request.POST.get('pic')
        data=user_edit(user_name=u_name,email=u_email,designation=desg,subarea=sub_area,Profile=profile,pic=pic)
        data.save()
        print(data.id)
        data=user_edit.objects.filter(id=data.id)
        return  render(request,'dash/profile.html',{'data':data})
    else:
        
        return  render(request,'dash/profile.html')