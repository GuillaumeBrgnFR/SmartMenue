# Étape 1 : Construire le frontend React
FROM node:16 AS frontend-builder
WORKDIR /app
COPY src/web-app/frontend/package*.json ./
RUN npm install
COPY src/web-app/frontend ./
RUN npm run build

# Étape 2 : Configurer l'environnement Python
FROM python:3.9-slim

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    tesseract-ocr \
    tesseract-ocr-fra \
    && rm -rf /var/lib/apt/lists/*

# Définir les variables d'environnement pour Flask
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=src/web-app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

WORKDIR /app

# Installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code du backend
COPY src src
COPY data data
COPY models models

# Copier la construction React dans le répertoire approprié
COPY --from=frontend-builder /app/build src/web-app/static
COPY --from=frontend-builder /app/build/index.html src/web-app/templates/index.html

# Démarrer l'application avec flask run
CMD ["flask", "run"]