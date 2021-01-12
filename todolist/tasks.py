from celery import shared_task
from todolist.models import Todo

@shared_task
def add(content):
    newtodo = Todo(content=content)
    newtodo.save()
    return None

@shared_task
def remove():
    return None