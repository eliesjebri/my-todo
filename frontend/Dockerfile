# Étape 1 : Build avec Node.js
FROM node:20-alpine AS build

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

COPY frontend/ .
RUN npm run build

# Étape 2 : Serveur NGINX
FROM nginx:1.25-alpine AS production

# Nettoyage
RUN rm -rf /usr/share/nginx/html/*

# Fichiers du build
COPY --from=build /app/dist /usr/share/nginx/html

# Config NGINX personnalisée (pas en dur non plus)
COPY frontend/nginx.template.conf /etc/nginx/templates/default.conf.template

# Dossier utilisé par nginx (peut rester tel quel)
ENV NGINX_PORT=80
ENV NGINX_HOST=0.0.0.0

CMD ["sh", "-c", "envsubst < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]
