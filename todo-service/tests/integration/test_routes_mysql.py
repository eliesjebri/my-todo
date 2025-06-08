import unittest
import os
from flask import Flask
from src.app import create_app
from src.persistence.db import db
from src.config import Config  # ✅ Centralisation de la config

@unittest.skipUnless(Config.ENV == "staging", "Test MySQL exécuté uniquement en staging")
class RoutesMySQLTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True

        # ✅ Connexion à la DB via Config
        self.app.config["SQLALCHEMY_DATABASE_URI"] = Config.DB_URI
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        self.client = self.app.test_client()

        with self.app.app_context():
            db.init_app(self.app)
            db.drop_all()
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_and_list_tasks_with_mysql(self):
        res = self.client.post("/todos", json={"title": "Test MySQL"})
        self.assertEqual(res.status_code, 201)

        res = self.client.get("/todos")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Test MySQL")

if __name__ == "__main__":
    unittest.main()
