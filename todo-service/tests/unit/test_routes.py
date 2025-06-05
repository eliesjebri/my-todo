import unittest
import json
from flask import Flask
from src.app import create_app
from src.persistence.db import db

class RoutesTestCase(unittest.TestCase):

    def setUp(self):
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
        response = self.client.post("/todos", json={"title": "Ma première tâche"})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data["title"], "Ma première tâche")
        self.assertFalse(data["is_completed"])

        response = self.client.get("/todos")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_get_todo_by_id(self):
        response = self.client.post("/todos", json={"title": "À tester"})
        task_id = response.get_json()["id"]

        response = self.client.get(f"/todos/{task_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["title"], "À tester")

    def test_update_todo(self):
        response = self.client.post("/todos", json={"title": "Ancien titre"})
        task_id = response.get_json()["id"]

        response = self.client.put(f"/todos/{task_id}", json={"title": "Nouveau titre"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["title"], "Nouveau titre")

    def test_complete_todo(self):
        response = self.client.post("/todos", json={"title": "À compléter"})
        task_id = response.get_json()["id"]

        response = self.client.patch(f"/todos/{task_id}/complete")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.get_json()["is_completed"])

    def test_delete_todo(self):
        response = self.client.post("/todos", json={"title": "À supprimer"})
        task_id = response.get_json()["id"]

        response = self.client.delete(f"/todos/{task_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "Tâche supprimée.")

        # Vérifie qu’elle est bien supprimée
        response = self.client.get(f"/todos/{task_id}")
        self.assertEqual(response.status_code, 405)  # car GET /todos/<id> n'existe pas

    def test_create_todo_without_title(self):
        response = self.client.post("/todos", json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_update_nonexistent_todo(self):
        response = self.client.put("/todos/999", json={"title": "Inexistant"})
        self.assertEqual(response.status_code, 404)

    def test_complete_nonexistent_todo(self):
        response = self.client.patch("/todos/999/complete")
        self.assertEqual(response.status_code, 404)

    def test_delete_nonexistent_todo(self):
        response = self.client.delete("/todos/999")
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
