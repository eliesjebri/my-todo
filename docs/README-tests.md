# 📦 README - Environnement de Test

Ce fichier documente comment exécuter les tests de l'application ToDo App dans l'environnement de développement **local** ou dans un conteneur **Docker**.

## 📁 Structure des tests

Les tests sont regroupés dans le dossier `todo-service/tests/` :

- `unit/`
  - `test_models.py` : test unitaire des modèles SQLAlchemy.
  - `test_service.py` : test unitaire des fonctions métier (services).
- `integration/`
  - `test_routes.py` : test d’intégration des routes en utilisant SQLite.
  - `test_routes_mysql.py` : test d’intégration des routes avec MySQL (staging).
  - `test_todos_performance.py` : test de performance configurable (GET et POST).

Les résultats des tests de performance sont exportés dans :
```
tests/results/perf_results.csv
```

---

## 🧪 Lancer les tests unitaires

En local :
```bash
python -m unittest discover -s todo-service/tests/unit
```

Avec Docker (dev) :
```bash
docker exec -it todo-dev python -m unittest discover -s tests/unit
```

---

## 🔗 Lancer les tests d’intégration (SQLite)

En local :
```bash
python -m unittest discover -s todo-service/tests/integration -p "test_routes.py"
```

Avec Docker (dev) :
```bash
docker exec -it todo-dev python -m unittest /app/tests/integration/test_routes.py
```

---

## 🗄 Lancer les tests d’intégration (MySQL - staging uniquement)

```bash
docker exec -it todo-staging python -m unittest /app/tests/integration/test_routes_mysql.py
```

> ✅ Ce test est **skippé automatiquement** sauf si la variable `ENV=staging`.

---

## 🚀 Test de performance

Le test POST + GET est centralisé dans `test_todos_performance.py`

Lancer avec le nombre d’itérations défini dans `.env` :

```bash
docker exec -it todo-staging python -m unittest /app/tests/integration/test_todos_performance.py
```

Le fichier CSV sera généré dans : `tests/results/perf_results.csv`

---

## 🧪 Ajouter un test

- Créer un nouveau fichier `test_*.py` dans le dossier approprié.
- Chaque test doit être une classe héritée de `unittest.TestCase`.

Exemple :

```python
import unittest

class SimpleTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)
```
