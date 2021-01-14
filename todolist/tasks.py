from celery import shared_task
from todolist.models import Todo

@shared_task
def add(content):
    newtodo = Todo(content=content)
    newtodo.save()
    return None

@shared_task
def remove(id):
    todelete = Todo.objects.get(pk=id)
    todelete.delete()
    return None