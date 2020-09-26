from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


def index(request):
    tasks = Task.objects.all()

    tasks_form = TaskForm()

    if request.method == 'POST':
        tasks_form = TaskForm(request.POST)
        if tasks_form.is_valid():
            tasks_form.save()
        return redirect('/')

    context = {'tasks': tasks, 'tasks_form': tasks_form}
    return render(request, 'tasks/index.html', context)
