from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from .models import *
from .forms import *


class IndexView(View):
    @staticmethod
    def get(request):
        tasks = Task.objects.all()
        tasks_form = TaskForm()

        context = {'tasks': tasks, 'tasks_form': tasks_form}
        return render(request, 'tasks/index.html', context)

    @staticmethod
    def post(request):
        tasks_form = TaskForm(request.POST)
        if tasks_form.is_valid():
            tasks_form.save()
        return redirect('/')


class UpdateTask(View):
    @staticmethod
    def get(request, primary_key):
        task = Task.objects.get(id=primary_key)
        task_form = TaskForm(instance=task)

        context = {'form': task_form}
        return render(request, 'tasks/update_task.html', context)

    @staticmethod
    def post(request, primary_key):
        task = Task.objects.get(id=primary_key)
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('/')
