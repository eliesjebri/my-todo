# 🏗️ Étape 1 : Builder Python allégé
FROM python:3.11-slim AS base

WORKDIR /app

# Variables de build
ARG BUILD_ENV=development
ENV ENV=${BUILD_ENV}

# Installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY src/ /app/src

# === STAGE DEV / TEST ===
FROM base AS dev

# Ajout du support Flask CLI
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl --fail http://localhost:5000/status || exit 1

CMD ["flask", "run"]

# === STAGE PROD / STAGING ===
FROM base AS prod 

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl --fail http://localhost:5000/status || exit 1

# On utilise Gunicorn en prod/staging
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.app:create_app()"]
