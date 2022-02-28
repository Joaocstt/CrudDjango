
from logging.config import valid_ident
from unicodedata import name
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages


def taskslist(request):
    conteudo_lista = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'lista': conteudo_lista})

def base(request):
    return render(request, 'tasks/base.html')

def taskView (request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

def newTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST) # Uma variável para preencher com os dados do POST. o var recebe os dados do TaskForm inserido pelo usuário.

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            messages.info(request, 'Tarefa adicionada com sucesso!')
            return redirect('/lista')
           
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})

def editTask (request, id): 
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task) # Variável recebe o formulário preenchido caso tenha.

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            messages.info(request, 'Tarefa editada com sucesso!')
            return redirect('/lista')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task':task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task':task})



def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')
    return redirect('/lista')

