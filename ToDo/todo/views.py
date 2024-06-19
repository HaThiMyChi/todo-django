from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def addTask(request):
    # task là cái name="task" ở input
    task = request.POST['task']
    Task.objects.create(task=task)
    # return HttpResponse('The form is submitted')
    return redirect('home')

def mark_as_done(request, pk):
    # primary key
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    # return HttpResponse(task)
    return redirect('home')