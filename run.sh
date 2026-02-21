#!/bin/bash

# Script de démarrage du projet Météo Toulouse (Mode Web)

echo "🌤️  Démarrage de l'application Web Météo Métro Toulouse..."
echo ""

# Se place automatiquement dans le dossier où se trouve le script (très important pour le partage)
cd "$(dirname "$0")"

# Vérifier ou créer l'environnement virtuel
if [ -d ".venv" ]; then
    echo "✅ Environnement virtuel trouvé."
    source .venv/bin/activate
else
    echo "⚠️  Environnement virtuel non trouvé. Création en cours..."
    python3 -m venv .venv
    source .venv/bin/activate
fi

echo "✅ Environnement activé."
echo ""
echo "📦 Vérification et installation des dépendances..."
# Installe les dépendances listées dans requirements.txt (dont flask et requests)
pip install -q -r requirements.txt

echo "✅ Dépendances prêtes."
echo ""
echo "🚀 Lancement du serveur Web..."
echo "👉 Ouvrez votre navigateur et allez sur : http://localhost:5001"
echo ""

# Lancer la NOUVELLE application Web
python web_app.py