from django.shortcuts import render
from todo.models import Task
def index(request):
    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)
    
    context={
        'tasks': tasks,
        'completed_tasks':completed_tasks
    }
    return render(request,"index.html",context)