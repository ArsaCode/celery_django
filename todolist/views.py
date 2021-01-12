from django.shortcuts import render

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
        form = CreateForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            tasks.add.delay(data)
            return render(request, "todolist/index.html", {
                "todos": todos,
            })
        else:
            return render(request, "todolist/add.html", {
            "addForm": AddForm()
            })

    else:
        return render(request, "todolist/add.html", {
            "addForm": AddForm()
        })