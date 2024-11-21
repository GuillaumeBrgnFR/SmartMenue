# Étape 1 : Construire le frontend React
FROM node:16 AS frontend-builder
WORKDIR /app
COPY src/web-app/frontend/package*.json ./
RUN npm install
COPY src/web-app/frontend ./
RUN npm run build

# Étape 2 : Configurer le backend Flask
FROM python:3.9-slim

# Définir les variables d'environnement pour Flask
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=src/web-app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

WORKDIR /app

# Installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source du backend
COPY src src
COPY data data
COPY models models

# Copier les fichiers construits par React dans le dossier statique de Flask
COPY --from=frontend-builder /app/build src/web-app/static
COPY --from=frontend-builder /app/build/index.html src/web-app/templates/index.html

# Exposer le port 5000
EXPOSE 5000

# Démarrer le serveur Flask
CMD ["flask", "run"]