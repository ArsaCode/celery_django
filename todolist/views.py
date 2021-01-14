from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from todolist.models import Todo
from todolist.forms import AddForm
from todolist import tasks

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, "todolist/index.html", {
        "todos": todos,
    })

def add(request):
    todos = Todo.objects.all()
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            tasks.add.delay(data.content)
            return HttpResponseRedirect(reverse('todolist:index'))
        else:
            return render(request, "todolist/add.html", {
            "addForm": AddForm()
            })

    else:
        return render(request, "todolist/add.html", {
            "addForm": AddForm()
        })

def delete(request, id):
    tasks.remove.delay(id)
    return HttpResponseRedirect(reverse('todolist:index'))