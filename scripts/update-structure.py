import os

# Structure recommandée
folders = [
    "todo-service/src/models",
    "todo-service/src/routes",
    "todo-service/src/services",
    "todo-service/src/persistence",
    "todo-service/tests/unit",
    "todo-service/tests/integration",
    "todo-service/tests/e2e"
]

files = [
    "todo-service/Dockerfile",
    "todo-service/.env",
    "todo-service/requirements.txt",
    "todo-service/src/__init__.py",
    "todo-service/src/app.py",
    "todo-service/src/config.py",
    "todo-service/src/models/task.py",
    "todo-service/src/routes/todos.py",
    "todo-service/src/services/todo_service.py",
    "todo-service/src/persistence/db.py",
    "todo-service/tests/unit/test_models.py",
    "todo-service/tests/unit/test_routes.py",
    "todo-service/tests/integration/test_db_connection.py",
    "todo-service/tests/e2e/test_end_to_end.py"
]

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"📁 Dossier créé : {path}")
    else:
        print(f"✅ Dossier déjà présent : {path}")

def create_file(path):
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write("")
        print(f"📄 Fichier créé : {path}")
    else:
        print(f"✅ Fichier déjà présent : {path}")

if __name__ == "__main__":
    print("🚀 Mise à jour de la structure de todo-service en cours...\n")

    for folder in folders:
        create_folder(folder)

    for file in files:
        create_file(file)

    print("\n✅ Structure mise à jour avec succès sur la branche develop.")

