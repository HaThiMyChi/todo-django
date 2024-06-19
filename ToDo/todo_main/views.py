from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    # return HttpResponse('<h1>Homepage</h1>')
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_completed=True)

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }

    # context tasks này nó được truyền trong file html để lấy data ra
    return render(request, 'home.html', context)