from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from .models import *
from .forms import *


class IndexView(View):
    def get(self, request):
        tasks = Task.objects.all()
        tasks_form = TaskForm()

        context = {'tasks': tasks, 'tasks_form': tasks_form}
        return render(request, 'tasks/index.html', context)

    def post(self, request):
        tasks_form = TaskForm(request.POST)
        if tasks_form.is_valid():
            tasks_form.save()
        return redirect('/')
