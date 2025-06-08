import unittest
import time
import os
import csv
from src.app import create_app
from dotenv import load_dotenv

load_dotenv(dotenv_path="/app/config/.env.staging")  # Chargement automatique

NB_ITERATIONS = int(os.getenv("NB_ITERATIONS", 10))
RESULTS_FILE = "tests/results/perf_results.csv"

class TodosPerformanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.makedirs(os.path.dirname(RESULTS_FILE), exist_ok=True)
        with open(RESULTS_FILE, mode="w", newline="") as file:
            csv.writer(file).writerow(["type", "itération", "temps(ms)"])

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_get_todos_performance(self):
        times = []
        for i in range(1, NB_ITERATIONS + 1):
            start = time.time()
            res = self.client.get("/todos")
            duration = (time.time() - start) * 1000
            times.append(duration)
            self.assertEqual(res.status_code, 200)
            with open(RESULTS_FILE, mode="a", newline="") as file:
                csv.writer(file).writerow(["GET", i, round(duration, 2)])
        avg = round(sum(times) / NB_ITERATIONS, 2)
        print(f"📊 GET /todos - Moyenne ({NB_ITERATIONS} reqs) : {avg} ms")
        self.assertLess(avg, 150, "GET /todos trop lent en moyenne")

    def test_post_todo_performance(self):
        times = []
        for i in range(1, NB_ITERATIONS + 1):
            payload = {"title": f"Perf todo #{i}"}
            start = time.time()
            res = self.client.post("/todos", json=payload)
            duration = (time.time() - start) * 1000
            times.append(duration)
            self.assertEqual(res.status_code, 201)
            with open(RESULTS_FILE, mode="a", newline="") as file:
                csv.writer(file).writerow(["POST", i, round(duration, 2)])
        avg = round(sum(times) / NB_ITERATIONS, 2)
        print(f"📊 POST /todos - Moyenne ({NB_ITERATIONS} reqs) : {avg} ms")
        self.assertLess(avg, 150, "POST /todos trop lent en moyenne")

if __name__ == "__main__":
    unittest.main()
