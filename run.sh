#!/bin/bash

# Script de démarrage 100% Docker

echo "🐳 Démarrage de Météo Métro Toulouse via Docker..."
echo ""

# Se placer automatiquement à la racine du projet
cd "$(dirname "$0")"

# Nom de notre image Docker
IMAGE_NAME="meteo-toulouse-app"

echo "📦 Étape 1 : Construction de l'image Docker..."
# Le tag -t donne un nom à l'image. Le "." signifie "utilise le Dockerfile d'ici"
docker build -t $IMAGE_NAME .

echo ""
echo "✅ Image prête !"
echo "🚀 Étape 2 : Lancement du serveur Web..."
echo "👉 Ouvrez votre navigateur et allez sur : http://localhost:5001"
echo "⚠️  (Pour arrêter le serveur proprement, appuyez sur Ctrl+C)"
echo "------------------------------------------------------"

# Lancement du conteneur
# --rm : Supprime le conteneur automatiquement quand on l'arrête (garde le PC propre)
# -p 5001:5001 : Relie le port 5001 de votre Mac au port 5001 du conteneur
docker run --rm -p 5001:5001 $IMAGE_NAME