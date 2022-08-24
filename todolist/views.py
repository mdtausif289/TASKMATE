from django.shortcuts import render,redirect
from .models import taskmate
from todolist.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def todolist(request):
    if request.method =="POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manage=request.user
            form.save()
        messages.success(request, "task added successfully")
        return redirect('todolist')
       
    else:
        all_task = taskmate.objects.filter(manage=request.user)
        paginator = Paginator(all_task, 10)
        page = request.GET.get('pg')
        all_task= paginator.get_page(page)
        return render(request, 'todolist.html', {"all_task":all_task})


def delete_task(request,task_id):
    task = taskmate.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
       messages.error(request, 'Access Restricted,You are not allowed')
    return redirect('todolist')

def complete_task(request,task_id):
    task = taskmate.objects.get(pk=task_id)
    if task.manage == request.user:
       task.done=True
       task.save()
    else:
        messages.error(request, 'Access Restricted,You are not allowed')
    return redirect('todolist')

def pending_task(request,task_id):
    task = taskmate.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect('todolist')

def edit_task(request,task_id):
    if request.method =="POST":
        task_obj = taskmate.objects.get(pk=task_id)
        form = TaskForm(request.POST or None,instance=task_obj)
        if form.is_valid():
            form.save()
        messages.success(request, "task updated successfully")
        return redirect('todolist')    
    else:
        task_obj = taskmate.objects.get(pk=task_id)
        return render(request, 'edit.html', {"task_obj":task_obj})


def home(request):
    return render(request, 'home.html')
@login_required
def contact(request):
    return render(request, 'contact.html')
@login_required
def about(request):
    return render(request, 'about.html')