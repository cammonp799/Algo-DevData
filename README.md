# 🚇 Météo Métro Toulouse (Data App Web & CLI)
---

Une application Fullstack (Backend Python + Frontend Web) permettant d'associer en temps réel les stations du réseau de métro de Toulouse (Tisséo) aux données des capteurs météorologiques les plus proches.

##  Démarrage Rapide (Docker)

Grâce à la conteneurisation Docker, aucune installation de Python ou d'environnement virtuel n'est requise sur votre machine.

### 1. Lancer l'application

```bash

git clone https://github.com/cammonp799/Algo-DevData.git
cd algo-devdata

```

# Construit l'image et lance le serveur

```bash
bash run.sh

```

--- Ouvrez ensuite votre navigateur à l'adresse : http://localhost:5001
    (Pour arrêter le serveur, faites simplement Ctrl+C dans le terminal).

--- Documentation Technique
    Pour en savoir plus sur les choix techniques, les algorithmes et l'architecture du projet, veuillez consulter les documents détaillés dans le dossier meteo_toulouse/src/docs/ :

--- Documentation Globale (DOCUMENTATION.md) :
    Fonctionnalités, exemples CLI, statistiques et accès à l'API OpenData.

--- Architecture & Concepts (architecture.md) : 
    Explication de la Clean Architecture, du Multithreading et des Design Patterns (Strategy, Decorator, Singleton).
 
--- Grille d'évaluation (CHECKLIST.md) : 
    Validation des principes SOLID, PEP8, et implémentation des structures de données (LinkedList, Queue).

--- Tests Qualité
    L'application est couverte par des tests unitaires (nécessite un environnement Python local) :

```bash

python -m pytest meteo_toulouse/src/tests/ -v

```
Développé par : Junior Chimène | 2026