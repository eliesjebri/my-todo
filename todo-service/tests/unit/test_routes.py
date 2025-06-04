import unittest
import json
from flask import Flask
from src.app import create_app
from src.persistence.db import db

class RoutesTestCase(unittest.TestCase):

    def setUp(self):
        # Crée une app Flask avec config test et DB in-memory
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.client = self.app.test_client()

        with self.app.app_context():
            db.init_app(self.app)
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_status_route(self):
        response = self.client.get("/status")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok"})

    def test_version_route(self):
        response = self.client.get("/version")
        self.assertEqual(response.status_code, 200)
        self.assertIn("version", response.json)

    def test_create_and_get_todo(self):
        # Créer une tâche
        response = self.client.post("/todos", json={"title": "Ma première tâche"})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data["title"], "Ma première tâche")
        self.assertFalse(data["is_completed"])

        # Récupérer les tâches
        response = self.client.get("/todos")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

if __name__ == '__main__':
    unittest.main()
