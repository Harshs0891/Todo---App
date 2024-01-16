from django.shortcuts import render,HttpResponseRedirect
from .forms import TaskRegistration
from .models import Tasks
# Create your views here.
def showlist(request):
    if request.method == 'POST':
        fm = TaskRegistration(request.POST)
        if fm.is_valid():
            ts = fm.cleaned_data['task']
            st = fm.cleaned_data['start_time']
            et = fm.cleaned_data['end_time']
            reg = Tasks(task = ts,start_time=st,end_time=et)
            reg.save()
            fm = TaskRegistration()
    else :
        fm = TaskRegistration()
    
    tasks = Tasks.objects.all()

    return render(request,'todo/list.html',{'form':fm,'tasks':tasks})


def updatelist(request,id):
    if request.method == 'POST':
        pi = Tasks.objects.get(pk=id)
        fm = TaskRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    if request.method == 'GET':
        pi = Tasks.objects.get(pk=id)
        fm = TaskRegistration(instance=pi)

    return render(request,'todo/update.html',{'id':id,'form':fm})


def deletelist(request,id):
    if request.method=='POST':
        reg = Tasks.objects.get(pk=id)
        reg.delete()
        return HttpResponseRedirect('/')