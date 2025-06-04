import unittest
from flask import Flask
from src.persistence.db import db, init_db
from src.models.task import Task

class TaskModelTestCase(unittest.TestCase):

    def setUp(self):
        # Crée une app Flask de test avec SQLite in-memory
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_task_creation(self):
        task = Task(title="Test unitaire")
        db.session.add(task)
        db.session.commit()

        self.assertIsNotNone(task.id)
        self.assertEqual(task.title, "Test unitaire")
        self.assertFalse(task.is_completed)

    def test_task_to_dict(self):
        task = Task(title="Exemple")
        db.session.add(task)
        db.session.commit()

        task_dict = task.to_dict()
        self.assertIn("id", task_dict)
        self.assertEqual(task_dict["title"], "Exemple")
        self.assertIn("created_at", task_dict)
        self.assertFalse(task_dict["is_completed"])

if __name__ == '__main__':
    unittest.main()
