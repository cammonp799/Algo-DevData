# 🏢 COMMENT AJOUTER D'AUTRES STATIONS

## 🎯 Le problème
Vous n'avez actuellement accès qu'à une seule station: **Paul Sabatier**

## ✅ La solution
Ajouter d'autres stations dans le fichier `config.py`

## 📍 Étapes pour ajouter une station

### Étape 1: Découvrir les stations disponibles
```bash
python discover_stations.py
```

Cela vous affichera toutes les stations météo disponibles sur OpenData Toulouse.

### Étape 2: Modifier config.py
Ouvrez `meteo_toulouse/config.py` et modifiez `stations_cibles`:

```python
"stations_cibles": [
    {
        "id": 37,
        "name": "Paul Sabatier",
        "dataset": "37-station-meteo-toulouse-universite-paul-sabatier",
        "description": "Station Météo Toulouse - Université Paul Sabatier"
    },
    # AJOUTEZ D'AUTRES STATIONS ICI:
    {
        "id": 42,
        "name": "Parc Compans Caffarelli",
        "dataset": "42-station-meteo-toulouse-parc-compans-cafarelli",
        "description": "Station Météo Toulouse - Parc Compans Caffarelli"
    },
    {
        "id": 45,
        "name": "Blagnac",
        "dataset": "45-station-meteo-toulouse-blagnac",
        "description": "Station Météo Toulouse - Blagnac (Aéroport)"
    },
]
```

### Étape 3: Tester
```bash
# Voir les stations disponibles
python -m meteo_toulouse.main --list

# Récupérer les données d'une station
python -m meteo_toulouse.main -s "Parc Compans"
python -m meteo_toulouse.main -s blagnac
```

## 📊 Stations connues (exemples)

Voici les stations généralement disponibles sur OpenData Toulouse:

| ID | Nom | Dataset |
|----|-----|---------|
| 37 | Paul Sabatier | 37-station-meteo-toulouse-universite-paul-sabatier |
| 42 | Parc Compans Caffarelli | 42-station-meteo-toulouse-parc-compans-cafarelli |
| ? | Blagnac | À chercher sur OpenData |
| ? | Francazal | À chercher sur OpenData |
| ? | Pech-David | À chercher sur OpenData |

## 🔗 Où trouver les datasets?

### Option 1: Via le script
```bash
python discover_stations.py
```

### Option 2: Sur le site web
1. Visitez: https://data.toulouse-metropole.fr/explore/
2. Cherchez: "meteo" ou "station"
3. Cliquez sur un dataset
4. Notez son ID (dans l'URL ou la page)
5. Cherchez le champ "dataset_id" dans les détails

### Option 3: Via l'API directement
```bash
curl "https://data.toulouse-metropole.fr/api/datasets/1.0/search/?q=meteo&rows=50"
```

## 📝 Format complet d'une station

```python
{
    "id": 37,                          # ID unique de la station
    "name": "Paul Sabatier",           # Nom court (pour --list et CLI)
    "dataset": "37-station-...",       # Dataset ID complet (depuis OpenData)
    "description": "Description..."    # Description longue
}
```

## 🧪 Vérifier une station

### 1. Vérifier que la station est bien ajoutée
```bash
python -m meteo_toulouse.main --list
```

### 2. Tester l'extraction de données
```bash
python -m meteo_toulouse.main -s "Nom de la station"
```

### 3. En cas d'erreur
- Vérifiez que le dataset ID est correct
- Vérifiez l'orthographe du nom
- Essayez avec le raccourci: `-s paul` au lieu de `-s "Paul Sabatier"`

## 💡 Astuces

### Recherche par mot-clé
```bash
# Ces commandes fonctionnent:
python -m meteo_toulouse.main -s paul      # Cherche "paul" dans les noms
python -m meteo_toulouse.main -s compans   # Cherche "compans"
python -m meteo_toulouse.main -s 37        # Cherche par ID
```

### Ajouter plusieurs stations
```python
"stations_cibles": [
    {"id": 37, "name": "Paul Sabatier", ...},
    {"id": 42, "name": "Parc Compans", ...},
    {"id": 45, "name": "Blagnac", ...},
    {"id": 50, "name": "Francazal", ...},
]
```

Puis:
```bash
python -m meteo_toulouse.main --list     # Affiche toutes les stations
python -m meteo_toulouse.main -s blagnac # Cherche "blagnac"
```

## 🎯 Cas d'usage complet

### Ajouter Blagnac
1. Découvrez l'ID:
   ```bash
   python discover_stations.py | grep -i blagnac
   ```

2. Modifiez config.py:
   ```python
   {
       "id": 42,
       "name": "Blagnac",
       "dataset": "42-station-meteo-toulouse-...",
       "description": "Station Aéroport Blagnac"
   }
   ```

3. Testez:
   ```bash
   python -m meteo_toulouse.main --list
   python -m meteo_toulouse.main -s blagnac
   ```

## ⚠️ Limitation actuelle

L'API OpenData Toulouse a plusieurs datasets différents. Chaque station peut avoir son propre dataset ID. Vous devez:

1. Trouver le bon dataset ID pour chaque station
2. L'ajouter dans la configuration
3. Tester que les données sont bien retournées

## 📚 Documentation OpenData Toulouse

- Site: https://data.toulouse-metropole.fr/
- Catalogue: https://data.toulouse-metropole.fr/explore/
- API: https://data.toulouse-metropole.fr/api/

---

**Question?** Utilisez `python discover_stations.py` pour découvrir les stations disponibles!
