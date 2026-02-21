# Application Météo Toulouse (Structurée)
---
## Description

✅ **Récupération des données météo** via API OpenData Toulouse  
✅ **Traitement avec une file d'attente** (Queue pattern)  
✅ **Stockage avec liste chaînée** pour les stations  
✅ **Affichage formaté** via décorateurs  
✅ **Configuration centralisée** des stations cibles  
✅ **Gestion des erreurs** et validation des données  

## Installation

### Prérequis
- Python 3.9+
- pip

### Étapes

```bash
```bash
# Cloner le projet
git clone https://github.com/cammonp799/Algo-DevData.git
cd algo-devdata

# Lancer le script d'installation et de démarrage automatique
bash run.sh

# Créer un environnement virtuel
python3 -m venv .venv
source .venv/bin/activate  # Sur macOS/Linux
# ou
.venv\Scripts\activate  # Sur Windows

# Installer les dépendances
pip install -r requirements.txt
```
```bash
### Lancer l'interface Web
python web_app.py
```

### Exemple de sortie
```
=== 🌤️ Application Météo Toulouse (Structurée) ===
📋 Chargement de la file d'attente avec 3 stations...
📥 [FILE] Traitement de l'extraction : toulouse-blagnac (api)
📡 Requête API envoyée : https://...
🏗️ Construction des objets et de la liste chaînée...
--- Parcours de la Liste Chaînée des Stations ---
=== 🌤️ Station météo : toulouse-blagnac ===
🕒 2025-02-20 12:30:00 | 🌡️ 8.5°C | 💧 72% | ⬇️ 1013 hPa | 🌧️ 0 mm | 💨 5 km/h
...
```

## Architecture

### Structure du Projet

```
meteo_toulouse/
├── __init__.py
├── main.py                      # Point d'entrée principal
├── config.py                    # Configuration centralisée
│
├── models/                      # Modèles de données
│   ├── Record.py               # Enregistrement météo (dataclass)
│   ├── Station.py              # Station météo (dataclass)
│   └── LinkedList.py           # Liste chaînée de stations
│
├── extractors/                 # Extraction de données
│   ├── ApiDataExtractor.py    # Extracteur API
│   └── ExtractionQueue.py     # File d'attente de tâches
│
├── mappers/                    # Mappage des données
│   └── RecordMapper.py         # Mapper Record (Pattern Strategy)
│
├── decorators/                 # Affichage (Pattern Decorator)
│   ├── StationDisplayDecorator.py
│   └── RecordDisplayDecorator.py
│
├── interfaces/                 # Contrats (ABC)
│   ├── IDataExtractor.py       # Interface extracteur
│   └── IDataMapper.py          # Interface mappeur
│
├── utils/                      # Utilitaires
│   └── Configuration.py        # Singleton de configuration
│
├── architecture/               # Documentation
│   ├── architecture.md
│   └── decisions.md
│
└── tests/                      # Tests unitaires
    ├── __init__.py
    ├── test_models.py
    ├── test_extractors.py
    └── test_mappers.py
```

## Structures de Données

### 1. **Liste Chaînée (LinkedList)** 📦
- **Classe**: `StationLinkedList`
- **Usage**: Stocker les stations météo avec accès séquentiel
- **Opérations**: `append()`, `display_all()`
- **Localisation**: `models/LinkedList.py`

### 2. **File d'Attente (Queue)** 🚪
- **Classe**: `ExtractionQueue`
- **Usage**: Gérer les tâches d'extraction en ordre FIFO
- **Opérations**: `enqueue()`, `dequeue()`, `is_empty()`, `process_queue()`
- **Localisation**: `extractors/ExtractionQueue.py`

### 3. **Dictionnaire (Dictionary)** 📚
- **Usage**: Configuration centralisée (`config.py`), stockage résultats extraction
- **Structure**: Clé-valeur pour stations cibles et données

## Design Patterns

### 1. **Strategy Pattern** 🎯
- **Classes**: `IDataExtractor`, `ApiDataExtractor`, `IDataMapper`, `RecordMapper`
- **Objectif**: Permettre différentes stratégies d'extraction et de mappage
- **Avantage**: Facilité d'ajouter de nouveaux extracteurs (CSV, JSON, etc.)

### 2. **Decorator Pattern** 🎨
- **Classes**: `StationDisplayDecorator`, `RecordDisplayDecorator`
- **Objectif**: Ajouter des responsabilités d'affichage sans modifier les modèles
- **Avantage**: Séparation des préoccupations (modèle vs affichage)

### 3. **Singleton Pattern** 🔒
- **Classe**: `Configuration`
- **Objectif**: Accès global à une configuration unique
- **Avantage**: Centralisation de la configuration

## Tests

### Exécuter les tests

```bash
# Tous les tests
python -m pytest tests/ -v

# Tests spécifiques
python -m pytest tests/test_models.py -v
python -m pytest tests/test_extractors.py -v

# Avec couverture de code
python -m pytest tests/ --cov=meteo_toulouse --cov-report=html
```

### Résultats attendus
- ✅ Modèles de données valides
- ✅ File d'attente FIFO
- ✅ Liste chaînée ordonnée
- ✅ Mappage correct des champs
- ✅ Extraction API fonctionnelle

## Documentation des Données

### Data Profiling: Record

| Champ | Type | Source API | Description |
|-------|------|-----------|-------------|
| heure_utc | datetime | heure_utc | Timestamp en UTC du relevé |
| temperature | float | temperature | Température en °C |
| humidite | float | humidite | Humidité relative en % |
| pression | float | pression | Pression atmosphérique en hPa |
| pluie | float | pluie | Cumul de pluie en mm |
| pluie_intensite_max | float | pluie_intensite_max | Intensité max en mm/h |
| direction_vent_moyen | float | direction_du_vecteur_vent_moyen | Direction en degrés (0-360°) |
| force_vent_moyen | float | force_vecteur_vent_moyen | Vitesse en km/h |
| direction_rafale_max | float | direction_du_vecteur_de_rafale_de_vent_max | Direction rafales (0-360°) |
| force_rafale_max | float | force_rafale_max | Vitesse rafales en km/h |

### Stations cibles

Les stations configurées (dans `config.py`):
- `toulouse-blagnac` - Aéroport Toulouse-Blagnac
- `toulouse-francazal` - Aéroport Toulouse-Francazal
- `toulouse-pech-david` - Station Toulouse Pech-David

### Source de données
- **API**: OpenData Toulouse
- **Dataset**: stations-meteo-en-temps-reel
- **URL Base**: https://data.toulouse-metropole.fr/api/records/1.0/search/
- **Format**: JSON
- **Fréquence MAJ**: Temps réel

## Respect des principes SOLID, KISS et DRY

- **SOLID**: Interfaces abstraites, responsabilité unique par classe
- **KISS**: Code simple et lisible, pas de surengineering
- **DRY**: Configuration centralisée, réutilisation de composants
- **YAGNI**: Toutes les classes et méthodes sont utilisées

## Norme PEP8

Le code respecte la norme PEP8:
- Noms de variables en snake_case
- Noms de classes en PascalCase
- Noms de fonctions en snake_case
- Longueur de ligne: 100 caractères max
- Docstrings pour classes et méthodes publiques

## Auteur
**Junior Chimène**  
---

**Dernière mise à jour**: Février 2025
