# ============================
# Étape 1 : Build Vite avec Node.js
FROM node:20-alpine AS builder

WORKDIR /app

COPY frontend/package.json ./
RUN npm install --package-lock-only
RUN npm install

COPY frontend/ .
# 👉 Corriger le problème d’entrée
COPY frontend/public/index.html ./index.html
COPY frontend/src ./src
COPY config/.env.frontend .env
RUN npm run build



# ============================
# Étape 2 : Serveur NGINX pour production
# ============================
FROM nginx:1.25-alpine AS app

# Nettoyage des fichiers par défaut
RUN rm -rf /usr/share/nginx/html/*

# Copier le build Vite
COPY --from=builder /app/dist /usr/share/nginx/html

# Configuration NGINX dynamique
COPY frontend/nginx.template.conf /etc/nginx/templates/default.conf.template

# Injecte les variables d’environnement depuis .env
ENV $(cat .env | xargs)

EXPOSE 80

CMD ["sh", "-c", "envsubst '${NGINX_PORT} ${NGINX_HOST}' < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]
