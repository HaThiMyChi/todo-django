from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def addTask(request):
    # task là cái name="task" ở input
    task = request.POST['task']
    Task.objects.create(task=task)
    # return HttpResponse('The form is submitted')
    return redirect('home')
