from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm  # мы создадим эту форму на следующем шаге

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'HW17/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'HW17/task_detail.html', {'task': task})

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'HW17/task_form.html', {'form': form})

def task_delete(request, pk):
    if request.method == 'POST':
        task = Task.objects.get(pk=pk)
        task.delete()
    return redirect('task_list')
