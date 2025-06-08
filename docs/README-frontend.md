# 🖥️ Frontend – ToDo App

Ce document explique comment builder, configurer et lancer l’interface utilisateur React du projet **ToDo App** à l’aide de Docker, Vite, et NGINX.

---

## 📁 Structure

```
my-todo/
├── frontend/
│   ├── src/
│   ├── public/
│   ├── Dockerfile
│   ├── nginx.template.conf
│   └── ...
├── config/
│   └── .env.frontend
├── docker-compose.frontend.yml
```

---

## ⚙️ Prérequis

- Docker
- Docker Compose

---

## 🌐 Fichier `.env.frontend`

Ce fichier contient les variables d’environnement utilisées au **moment du build** par Vite, et au **runtime** par NGINX.

Exemple :

```env
VITE_API_URL=http://todo-service:5001
VITE_ENV=development
VITE_APP_NAME=ToDo App (Dev)
VITE_FRONT_VERSION=0.1.0-dev
```

---

## 🐳 Build & Run avec Docker Compose

```bash
docker compose -f docker-compose.frontend.yml up -d --build
```

⏳ Cela :

1. Copie `.env.frontend` en `.env` lors du build Vite.
2. Compile le frontend via Vite (`npm run build`).
3. Servez l’app via un container NGINX avec une configuration injectée dynamiquement.
4. Expose l’interface sur [http://localhost:5173](http://localhost:5173)

---

## ⚠️ Important

- Le backend `todo-service` doit être démarré en parallèle (ex: via `docker-compose.staging.yml`)
- Toutes les variables doivent être centralisées dans `config/.env.frontend`.

---

## ✅ Bonnes pratiques respectées

- 📦 Architecture 12factor
- 🐳 Build multistage Docker
- 🔒 Aucun secret ou URL codé en dur
- 📁 Configurations centralisées dans `config/`

