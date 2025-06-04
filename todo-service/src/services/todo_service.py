from src.models.task import Task
from src.persistence.db import get_db

db = get_db()

def get_all_tasks():
    tasks = Task.query.all()
    return [task.to_dict() for task in tasks]

def get_task_by_id(task_id):
    return Task.query.get(task_id)

def create_task(title):
    task = Task(title=title)
    db.session.add(task)
    db.session.commit()
    return task.to_dict()

def update_task(task_id, title=None):
    task = get_task_by_id(task_id)
    if not task:
        return None

    if title:
        task.title = title
    db.session.commit()
    return task.to_dict()

def complete_task(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return None

    task.is_completed = True
    db.session.commit()
    return task.to_dict()

def delete_task(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return False

    db.session.delete(task)
    db.session.commit()
    return True
