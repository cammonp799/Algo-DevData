# 🚀 QUICK START GUIDE

## Installation rapide (2 minutes)

### 1. Prérequis
- Python 3.9+ installé
- pip installé
- Terminal ouvert

### 2. Installation
```bash
# Naviguer au projet
cd /Users/juniorchimene/PycharmProjects/project_weather_toulouse

# Créer un environnement virtuel
python3 -m venv .venv

# Activer l'environnement (macOS/Linux)
source .venv/bin/activate

# Activer l'environnement (Windows)
.venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

### 3. Lancer l'application
```bash
python -m meteo_toulouse.main
```

### 4. Lancer les tests
```bash
pytest meteo_toulouse/tests/ -v
```

---

## Fichiers importants

| Fichier | Objectif |
|---------|----------|
| `README.md` | Documentation complète |
| `IMPROVEMENTS.md` | Résumé des améliorations |
| `CHECKLIST.md` | Vérification des critères |
| `ROADMAP.md` | Améliorations futures |
| `meteo_toulouse/main.py` | Point d'entrée |
| `meteo_toulouse/config.py` | Configuration |
| `meteo_toulouse/tests/` | Tests unitaires |

---

## Structure du projet

```
project_weather_toulouse/
├── README.md                    # Documentation complète
├── requirements.txt             # Dépendances Python
├── pytest.ini                   # Configuration pytest
├── .pylintrc                    # Configuration pylint
├── CHECKLIST.md                 # Checklist d'évaluation
├── IMPROVEMENTS.md              # Résumé des améliorations
├── ROADMAP.md                   # Feuille de route
│
└── meteo_toulouse/
    ├── __init__.py
    ├── __main__.py              # Point d'entrée (python -m)
    ├── main.py                  # Fonction principale
    ├── config.py                # Configuration centralisée
    │
    ├── models/                  # Modèles de données
    │   ├── Record.py           # Enregistrement météo
    │   ├── Station.py          # Station météo
    │   └── LinkedList.py       # Liste chaînée
    │
    ├── extractors/             # Extraction de données
    │   ├── ApiDataExtractor.py # Extracteur API
    │   └── ExtractionQueue.py  # File d'attente FIFO
    │
    ├── mappers/                # Transformation de données
    │   └── RecordMapper.py     # Mapper Record
    │
    ├── decorators/             # Affichage formaté
    │   ├── StationDisplayDecorator.py
    │   └── RecordDisplayDecorator.py
    │
    ├── interfaces/             # Contrats (ABC)
    │   ├── IDataExtractor.py   # Interface extracteur
    │   └── IDataMapper.py      # Interface mapper
    │
    ├── utils/                  # Utilitaires
    │   └── Configuration.py    # Singleton Configuration
    │
    ├── architecture/           # Documentation
    │   ├── architecture.md     # Vue d'ensemble
    │   └── decisions.md        # Décisions techniques
    │
    └── tests/                  # Tests unitaires
        ├── test_models.py      # Tests modèles (13 tests)
        ├── test_extractors.py  # Tests extracteurs (10 tests)
        └── test_mappers.py     # Tests mappers (8 tests)
```

---

## Commandes principales

### Application
```bash
# Lancer l'app
python -m meteo_toulouse.main

# Ou directement
python meteo_toulouse/main.py
```

### Tests
```bash
# Tous les tests
pytest meteo_toulouse/tests/ -v

# Tests spécifiques
pytest meteo_toulouse/tests/test_models.py -v
pytest meteo_toulouse/tests/test_extractors.py -v

# Avec couverture
pytest --cov=meteo_toulouse --cov-report=html
```

### Qualité du code
```bash
# PyLint
pylint meteo_toulouse

# Avec config
pylint meteo_toulouse --rcfile=.pylintrc
```

---

## Principales classes

### Modèles
```python
from meteo_toulouse.models.Record import Record
from meteo_toulouse.models.Station import Station
from meteo_toulouse.models.LinkedList import StationLinkedList
```

### Extraction
```python
from meteo_toulouse.extractors.ApiDataExtractor import ApiDataExtractor
from meteo_toulouse.extractors.ExtractionQueue import ExtractionQueue
```

### Mappage
```python
from meteo_toulouse.mappers.RecordMapper import RecordMapper
```

### Affichage
```python
from meteo_toulouse.decorators.StationDisplayDecorator import StationDisplayDecorator
```

---

## Exemple d'utilisation simple

```python
from meteo_toulouse.extractors.ApiDataExtractor import ApiDataExtractor
from meteo_toulouse.mappers.RecordMapper import RecordMapper
from meteo_toulouse.models.Station import Station

# Créer l'extracteur et le mappeur
extractor = ApiDataExtractor()
mapper = RecordMapper()

# Extraire les données
data = extractor.extract("toulouse-blagnac")

# Créer une station
station = Station(nom="toulouse-blagnac")

# Mapper et ajouter les records
if data and "records" in data:
    for record_data in data["records"]:
        record = mapper.to_object(record_data)
        station.add_record(record)

# Afficher
print(f"Station: {station.nom}")
print(f"Nombre de records: {len(station.records)}")
```

---

## Dépannage

### Erreur: Module not found
```bash
# Vérifier que l'environnement est activé
source .venv/bin/activate
```

### Erreur: No module named 'requests'
```bash
# Réinstaller les dépendances
pip install -r requirements.txt
```

### Tests ne trouvent pas le module
```bash
# Exécuter depuis le répertoire racine du projet
cd /Users/juniorchimene/PycharmProjects/project_weather_toulouse
pytest meteo_toulouse/tests/
```

---

## Performance

- **Temps d'exécution**: ~2-3 secondes (avec requêtes API)
- **Nombre de tests**: 31
- **Taux de succès**: 100% ✅

---

## Support et documentation

- 📖 **README.md**: Documentation complète
- ✅ **CHECKLIST.md**: Vérification des critères
- 📋 **IMPROVEMENTS.md**: Résumé des améliorations
- 🚀 **ROADMAP.md**: Améliorations futures
- 🏗️ **architecture/**: Documentation technique

---

**Prêt à utiliser!** 🎉
