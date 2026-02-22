# 🚇 Météo Métro Toulouse (Data App Web & CLI)
---
## 📝 Description

Une application Fullstack (Backend structuré + Frontend Web) permettant d'associer en temps réel les stations du réseau de métro de Toulouse (Tisséo) aux données des capteurs météorologiques les plus proches.

Cette application a été conçue avec une approche **Production-Ready** :
✅ **Performances extrêmes** : Appels API asynchrones via Multithreading (`concurrent.futures`).
✅ **Interface Web moderne** : Carte interactive (Leaflet.js) et affichage dynamique "Split-Screen" (Flask).
✅ **Déploiement DevOps** : Conteneurisation 100% Dockerisée.
✅ **Clean Architecture** : Séparation stricte entre la logique métier (`core`), le web (`web`) et la configuration (`config`).
✅ **Design Patterns** : Utilisation de Strategy, Decorator et Singleton.

---

## 🚀 Démarrage Rapide (Recommandé)

Grâce à Docker, vous n'avez besoin d'installer ni Python, ni d'environnements virtuels pour tester ce projet.

### Prérequis
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installé et allumé.

### Lancement en 1 commande
```bash
# Cloner le projet
git clone [https://github.com/votre-pseudo/algo-devdata.git](https://github.com/votre-pseudo/algo-devdata.git)
cd algo-devdata
```

# Construire l'image et lancer le serveur (Mac/Linux)
```bash run.sh
👉 Ouvrez ensuite votre navigateur à l'adresse : http://localhost:5001
```
(Pour arrêter le serveur, faites simplement Ctrl+C dans le terminal).

🏗️ Architecture du Projet (Clean Architecture)
Le code est organisé selon les standards de l'industrie pour garantir sa maintenabilité :

Plaintext
algo-devdata/
├── Dockerfile                    # 🐳 Recette de construction de l'environnement
├── run.sh                        # 🚀 Script de lancement Docker
├── requirements.txt              # 📦 Dépendances Python
│
└── meteo_toulouse/
    └── src/                          
        ├── web/                  # 🌐 Interface Web (Frontend & Routeur)
        │   ├── static/           #   ↳ CSS, JS (Carte Leaflet)
        │   ├── templates/        #   ↳ HTML
        │   └── web_app.py        #   ↳ Serveur Flask (Point d'entrée)
        │
        ├── core/                 # 🧠 Logique Métier (Backend)
        │   ├── extractors/       #   ↳ Appels API & File d'attente (Queue)
        │   ├── mappers/          #   ↳ Transformation JSON -> Objets Python
        │   ├── models/           #   ↳ Record, Station, LinkedList
        │   ├── decorators/       #   ↳ Formatage d'affichage (CLI)
        │   └── utils/            #   ↳ Singleton (Configuration)
        │
        ├── config/               # ⚙️ Configurations centralisées
        │   ├── config.py         #   ↳ URL de l'API OpenData
        │   └── metro_stations_config.py # ↳ Mapping Lignes de métro / Capteurs
        │
        ├── tests/                # 🧪 Tests unitaires (Pytest)
        └── docs/                 # 📚 Documentation technique détaillée
        
🛠️ Stack Technique & Concepts

1. Structures de Données
File d'Attente (Queue) : Gère les tâches d'extraction API en ordre FIFO pour éviter de saturer le réseau.

Liste Chaînée (LinkedList) : Stocke les stations météo avec un accès séquentiel optimisé (models/LinkedList.py).

Dictionnaires & Sets : Filtrage et indexation ultra-rapide des stations cibles.

2. Design Patterns Implémentés
Strategy Pattern : Permet de changer la méthode d'extraction de données sans casser le code (IDataExtractor, ApiDataExtractor).

Decorator Pattern : Ajoute des responsabilités d'affichage sans modifier les Modèles de base (StationDisplayDecorator).

Singleton Pattern : Accès global et unique à la configuration de l'API (utils/Configuration.py).

3. OpenData Toulouse
API : OpenData Toulouse Métropole (v2.1)

Dataset : stations-meteo-en-temps-reel (Couverture de plus de 50 capteurs).

Format : JSON Temps réel.

🧪 Tests & Qualité du code
Le code respecte strictement la norme PEP8 (vérifié via pylint) et les principes SOLID, KISS et DRY.

Pour exécuter les tests manuellement (nécessite Python d'installé localement) :

 ``` Bash
python -m pytest meteo_toulouse/src/tests/ -v
```
Développé par : Junior Chimène | 2026