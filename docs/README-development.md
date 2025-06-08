# 🧪 Environnement de Développement – Todo App

Ce document décrit comment installer, exécuter et développer localement l'application Todo App dans un environnement de développement standardisé.

## 📁 Structure générale

```
my-todo/
├── todo-service/
│   ├── src/
│   ├── tests/
│   └── Dockerfile
├── config/
│   └── .env.dev
├── docker-compose.dev.yml
├── docs/
└── README-development.md
```

## 🛠️ Prérequis

- Python 3.11+
- [Docker](https://www.docker.com/)
- [Docker Compose V2](https://docs.docker.com/compose/)
- Un éditeur de code comme VSCode ou PyCharm

---

## 🚀 Lancer l'environnement avec Docker

L'environnement de développement est basé sur **SQLite** et se lance avec :

```bash
docker compose --env-file ./config/.env.dev -f docker-compose.dev.yml up -d --build
```

### Fichiers principaux :

- `Dockerfile` : définit l'image pour le service `todo-service`
- `docker-compose.dev.yml` : configuration multi-conteneurs pour le dev
- `config/.env.dev` : variables d'environnement (utilise SQLite)

Exemple de contenu `.env.dev` :

```env
ENV=development
DEBUG=True
PORT=5000
VERSION=0.1.0-dev
SQLITE_URI=sqlite:////etc/todo.db
```

---

## ⚙️ Accès à l'application

Une fois lancée :

- Frontend React (si disponible) : http://localhost:3000
- Backend Flask API : http://localhost:5000

---

## 🧪 Lancer les tests

Tous les tests utilisent SQLite dans l’environnement `dev`.

### 1. Tests unitaires :

```bash
docker exec -it todo-dev python -m unittest discover -s tests/unit
```

### 2. Tests d’intégration :

```bash
docker exec -it todo-dev python -m unittest discover -s tests/integration -p "test_routes.py"
```

---

## 🧹 Astuces pour le développement

- Utilise `volumes:` dans `docker-compose.dev.yml` pour du code **hot-reloadé** dans le conteneur
- Active les logs de développement : `FLASK_DEBUG=True`
- Garde les dépendances propres dans `requirements.txt`

---

## 📂 Volumes montés automatiquement

- Code source : `./todo-service/src` → `/app/src`
- Tests : `./todo-service/tests` → `/app/tests`
- Config : `./config` → `/app/config`
- Base SQLite persistante : `./todo-service/data/todo.db` → `/etc/todo.db`

---

## 🔄 Arrêter l'environnement

```bash
docker compose -f docker-compose.dev.yml down
```

