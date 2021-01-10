from celery import shared_task
from todolist.models import Todo

@shared_task
def add():
    return None

def remove():
    return None