from django.shortcuts import render
from todolist.models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, "todolist/index.html", {
        "todos": todos,
    })