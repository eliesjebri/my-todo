import unittest
from flask import Flask
from src.persistence.db import db, init_db
from src.models.task import Task
from src.services.todo_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    complete_task,
)

class TodoServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app_context = self.app.app_context()
        self.app_context.push()

        init_db(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_and_retrieve_task(self):
        """✅ Vérifie la création et récupération d'une tâche par ID"""
        task = create_task("Tâche test")
        self.assertIsNotNone(task["id"])

        retrieved = get_task_by_id(task["id"])
        self.assertEqual(retrieved["title"], "Tâche test")

    def test_complete_task(self):
        """✅ Vérifie que complete_task() met bien à jour is_completed"""
        task = create_task("À compléter")
        self.assertFalse(task["is_completed"])

        completed = complete_task(task["id"])
        self.assertTrue(completed["is_completed"])

