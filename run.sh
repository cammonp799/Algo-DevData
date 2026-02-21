#!/bin/bash

# Script de démarrage du projet Météo Toulouse

echo "🌤️  Démarrage de l'application Météo Toulouse..."
echo ""

# Naviguer au projet
cd /Users/juniorchimene/PycharmProjects/project_weather_toulouse

# Vérifier que l'environnement est activé
if [ -d ".venv" ]; then
    echo "✅ Environnement virtuel trouvé"
    source .venv/bin/activate
else
    echo "⚠️  Environnement virtuel non trouvé. Création..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -q -r requirements.txt
fi

echo "✅ Environnement activé"
echo ""
echo "📦 Installation des dépendances..."
pip install -q -r requirements.txt

echo "✅ Dépendances installées"
echo ""
echo "🚀 Lancement de l'application..."
echo ""

# Lancer l'application
python -m meteo_toulouse.main

echo ""
echo "✅ Application terminée"
