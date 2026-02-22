# Utilise une image Python légère officielle
FROM python:3.10-slim

# Définit le dossier de travail dans le conteneur
WORKDIR /app

# Copie le fichier des dépendances et les installe
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le reste du projet
COPY . .

# Expose le port utilisé par Flask
EXPOSE 5001

# Commande pour lancer l'application
CMD ["python", "meteo_toulouse/src/web/web_app.py"]