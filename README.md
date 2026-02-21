\"\"\"\nApplication Web Flask pour Météo Toulouse\nFrontend moderne pour visualiser les données météo en temps réel\n\"\"\"\n\nfrom flask import Flask, render_template, jsonify\nimport sys\nimport os\n\n# Ajouter le chemin du projet\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\n\nfrom meteo_toulouse.extractors.ApiDataExtractor import ApiDataExtractor\nfrom meteo_toulouse.extractors.ExtractionQueue import ExtractionQueue\nfrom meteo_toulouse.mappers.RecordMapper import RecordMapper\nfrom meteo_toulouse.models.LinkedList import StationLinkedList\nfrom meteo_toulouse.config import STATIONS_CIBLES\n\napp = Flask(__name__, template_folder='templates', static_folder='static')\n\n\ndef get_weather_data():\n    \"\"\"Récupère les données météo de toutes les stations.\"\"\"\n    stations_data = []\n    \n    # Créer la file d'attente et l'extracteur\n    queue = ExtractionQueue()\n    extractor = ApiDataExtractor()\n    mapper = RecordMapper()\n    \n    # Ajouter les stations à la file\n    for station_id in STATIONS_CIBLES:\n        queue.enqueue(station_id, \"api\")\n    \n    # Traiter la file\n    while not queue.is_empty():\n        task = queue.dequeue()\n        station_id = task[\"station_id\"]\n        \n        try:\n            raw_data = extractor.extract(station_id)\n            if raw_data:\n                records = mapper.map(raw_data)\n                \n                # Prendre le dernier enregistrement (le plus récent)\n                if records:\n                    latest_record = records[0] if isinstance(records, list) else records\n                    \n                    station_info = {\n                        \"id\": station_id,\n                        \"name\": station_id.replace(\"-\", \" \").title(),\n                        \"temperature\": getattr(latest_record, 'temperature', None),\n                        \"humidite\": getattr(latest_record, 'humidite', None),\n                        \"pression\": getattr(latest_record, 'pression', None),\n                        \"pluie\": getattr(latest_record, 'pluie', 0),\n                        \"vent\": getattr(latest_record, 'force_vent_moyen', None),\n                        \"direction_vent\": getattr(latest_record, 'direction_vent_moyen', None),\n                        \"heure\": str(getattr(latest_record, 'heure_utc', 'N/A'))\n                    }\n                    stations_data.append(station_info)\n        except Exception as e:\n            print(f\"Erreur pour {station_id}: {e}\")\n            stations_data.append({\n                \"id\": station_id,\n                \"name\": station_id.replace(\"-\", \" \").title(),\n                \"error\": str(e)\n            })\n    \n    return stations_data\n\n\n@app.route('/')\ndef index():\n    \"\"\"Page principale.\"\"\"\n    return render_template('index.html')\n\n\n@app.route('/api/weather')\ndef api_weather():\n    \"\"\"API endpoint pour les données météo.\"\"\"\n    try:\n        data = get_weather_data()\n        return jsonify({\"success\": True, \"stations\": data})\n    except Exception as e:\n        return jsonify({\"success\": False, \"error\": str(e)})\n\n\n@app.route('/api/stations')\ndef api_stations():\n    \"\"\"Liste des stations disponibles.\"\"\"\n    return jsonify({\"stations\": list(STATIONS_CIBLES)})\n\n\nif __name__ == '__main__':\n    print(\"🌤️ Démarrage du serveur Météo Toulouse...\")\n    print(\"📡 Accédez à http://localhost:5000\")\n    app.run(debug=True, host='0.0.0.0', port=5000)\n

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
# Cloner ou naviguer vers le projet
cd /Users/juniorchimene/PycharmProjects/project_weather_toulouse

# Créer un environnement virtuel
python3 -m venv .venv
source .venv/bin/activate  # Sur macOS/Linux
# ou
.venv\Scripts\activate  # Sur Windows

# Installer les dépendances
pip install -r requirements.txt
```

## Utilisation

### Lancer l'application

```bash
# Via module principal
python -m meteo_toulouse.main

# Ou directement
python meteo_toulouse/main.py
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
