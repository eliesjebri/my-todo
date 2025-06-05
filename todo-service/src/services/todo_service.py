from src.models.task import Task
from src.persistence.db import db
from datetime import datetime

def get_all_tasks():
    tasks = Task.query.all()
    return [task.to_dict() for task in tasks]

def get_task_by_id(task_id):
    task = Task.query.get(task_id)
    return task.to_dict() if task else None

def create_task(title):
    task = Task(title=title)
    db.session.add(task)
    db.session.commit()
    return task.to_dict()

def update_task(task_id, title=None):
    task = Task.query.get(task_id)
    if not task:
        return None
    if title:
        task.title = title
        task.updated_at = datetime.utcnow()
        db.session.commit()
    return task.to_dict()

def complete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return None
    task.is_completed = True
    task.updated_at = datetime.utcnow()
    db.session.commit()
    return task.to_dict()

def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return False
    db.session.delete(task)
    db.session.commit()
    return True
