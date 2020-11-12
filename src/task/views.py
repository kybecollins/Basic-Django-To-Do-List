from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import *
from .forms import *

# Create your views here.

def index(request):
    task = Tasks.objects.all()
    form = TasksForm()

    if request.method =="POST":
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ("/")


    context = {'task':task,'form':form}
    return render(request, 'task/home.html',context)

def updateTask(request,pk):
    tasks = Tasks.objects.get(id=pk)

    form = TasksForm(instance=tasks)

    if request.method =="POST":
        form = TasksForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
            messages.success(request,('Update Successful !! '))
        return redirect ("/")


    context = {'form':form}

    return render(request, 'task/update.html',context)

def deleteTask(request, pk):
    item = Tasks.objects.get(id=pk)
    item.delete()
    messages.success(request,('Task was Deleted Successfully !! '))
    return redirect('home')

    # if request.method =="POST":
    #     item.delete()
    #     return redirect ("/")


    # context = {"item":item}

    # return render(request, 'task/delete.html',context)
