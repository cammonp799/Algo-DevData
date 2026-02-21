#!/bin/bash

# Script de démonstration des nouvelles fonctionnalités CLI

echo "🌤️  DÉMONSTRATION DES NOUVELLES FONCTIONNALITÉS"
echo ""
echo "=================================================="
echo "TEST 1: Afficher l'aide"
echo "=================================================="
echo ""
echo "Commande: python -m meteo_toulouse.main --help"
echo ""

cd /Users/juniorchimene/PycharmProjects/project_weather_toulouse

python -m meteo_toulouse.main --help

echo ""
echo "=================================================="
echo "TEST 2: Lister les stations disponibles"
echo "=================================================="
echo ""
echo "Commande: python -m meteo_toulouse.main --list"
echo ""

python -m meteo_toulouse.main --list

echo ""
echo "=================================================="
echo "TEST 3: Récupérer les données d'une station"
echo "=================================================="
echo ""
echo "Commande: python -m meteo_toulouse.main --station 'Paul Sabatier' --limit 30"
echo ""

python -m meteo_toulouse.main --station "Paul Sabatier" --limit 30

echo ""
echo "=================================================="
echo "TEST 4: Utiliser le raccourci -s"
echo "=================================================="
echo ""
echo "Commande: python -m meteo_toulouse.main -s paul -v"
echo ""

python -m meteo_toulouse.main -s paul -v

echo ""
echo "✅ Tests terminés!"
