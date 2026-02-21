# 🎯 NOUVELLES FONCTIONNALITÉS CLI

## ✨ Qu'est-ce qui a changé?

Vous pouvez maintenant:
- ✅ Passer le nom d'une station en argument CLI
- ✅ Recevoir les données en direct sans interaction
- ✅ Lister les stations disponibles
- ✅ Contrôler le nombre de records affichés
- ✅ Mode interactif si aucun argument n'est fourni

## 📋 Utilisation

### 1. Mode interactif (par défaut)
```bash
python -m meteo_toulouse.main
```

L'application vous demandera:
- Quelle station choisir
- Combien de records afficher

### 2. Mode ligne de commande avec station
```bash
python -m meteo_toulouse.main --station "Paul Sabatier"
python -m meteo_toulouse.main -s paul
python -m meteo_toulouse.main -s 37
```

**Sortie**: Affiche directement les données sans interaction

### 3. Lister les stations disponibles
```bash
python -m meteo_toulouse.main --list
python -m meteo_toulouse.main -l
```

**Sortie**:
```
======================================================================
📍 STATIONS MÉTÉOROLOGIQUES DISPONIBLES
======================================================================

  ID: 37  | Nom: Paul Sabatier

Utilisation: python -m meteo_toulouse.main --station <nom>
             python -m meteo_toulouse.main -s <nom>
```

### 4. Limiter le nombre de records
```bash
python -m meteo_toulouse.main --station "Paul Sabatier" --limit 20
python -m meteo_toulouse.main -s paul --limit 50
```

### 5. Mode verbeux
```bash
python -m meteo_toulouse.main --station "Paul Sabatier" --verbose
python -m meteo_toulouse.main -s paul -v
```

Affiche plus de détails sur le traitement

### 6. Afficher l'aide
```bash
python -m meteo_toulouse.main --help
python -m meteo_toulouse.main -h
```

## 🎨 Exemples complets

### Exemple 1: Obtenir les 25 derniers relevés
```bash
$ python -m meteo_toulouse.main --station "Paul Sabatier" --limit 25

======================================================================
🌤️  Application Météo Toulouse - Station: Paul Sabatier
======================================================================

📥 Extraction des données...

✅ Paul Sabatier: 25 record(s) trouvé(s)

--- Parcours de la Liste Chaînée des Stations ---
 Traitement du nœud pour : Paul Sabatier

=== 🌤️ Station météo : Paul Sabatier ===
🕒 2022-01-18 18:30:00+00:00  🌡️ 1.8C  💧 84%  ⬇️ 112100 hPa  🌧️ 0 mm  💨 0 km/h
🕒 2022-01-13 13:30:00+00:00  🌡️ 0.5C  💧 85%  ⬇️ 115500 hPa  🌧️ 0 mm  💨 2 km/h
...
```

### Exemple 2: Mode interactif
```bash
$ python -m meteo_toulouse.main

======================================================================
🌤️  Application Météo Toulouse (MODE INTERACTIF)
======================================================================

📍 Stations disponibles:
  37: Paul Sabatier

Choisissez une station (ID ou nom, ou 'q' pour quitter): paul
Nombre de records à afficher (défaut: 100, max: 100): 10

======================================================================
🌤️  Application Météo Toulouse - Station: Paul Sabatier
======================================================================

✅ Paul Sabatier: 10 record(s) trouvé(s)
...
```

### Exemple 3: Vérifier les stations avec raccourci
```bash
$ python -m meteo_toulouse.main -l

======================================================================
📍 STATIONS MÉTÉOROLOGIQUES DISPONIBLES
======================================================================

  ID:  37 | Nom: Paul Sabatier

Utilisation: python -m meteo_toulouse.main --station <nom>
             python -m meteo_toulouse.main -s <nom>
```

## 📊 Options disponibles

| Option | Raccourci | Type | Défaut | Description |
|--------|-----------|------|--------|-------------|
| `--station` | `-s` | str | None | Nom ou ID de la station |
| `--list` | `-l` | bool | False | Lister les stations |
| `--limit` | - | int | 100 | Nombre max de records |
| `--verbose` | `-v` | bool | False | Mode verbeux |
| `--help` | `-h` | bool | False | Afficher l'aide |

## 🔧 Implémentation technique

### Fonctions ajoutées:

1. **parse_arguments()** → Analyse les arguments CLI
   - Utilise `argparse` pour robustesse
   - Support des raccourcis (-s, -l, -v)
   - Message d'aide détaillé avec exemples

2. **get_available_stations()** → Retourne dict des stations
   - Structure: `{id: nom}`

3. **list_stations()** → Affiche les stations
   - Formatage lisible
   - Instructions d'utilisation

4. **process_station_data()** → Traite une station spécifique
   - Extraction des données
   - Mappage et affichage
   - Optionnel: mode verbeux

5. **main_interactive()** → Mode interactif
   - Demande à l'utilisateur de choisir
   - Validation des entrées
   - Gestion des erreurs (Ctrl+C)

6. **main()** → Orchestration principale
   - Gère les arguments CLI
   - Dirige vers le bon mode

## ✅ Avantages

✅ **Facilité d'utilisation**: Pas besoin de connaître la structure interne  
✅ **Flexibilité**: CLI ou mode interactif  
✅ **Contrôle**: Limiter les données affichées  
✅ **Clarté**: Messages d'erreur explicites  
✅ **Documentation**: Aide intégrée complète  
✅ **Robustesse**: Gestion des entrées invalides  

## 🎯 Cas d'usage

### Cas 1: Script automatisé
```bash
#!/bin/bash
for station in "paul" "toulouse"; do
    python -m meteo_toulouse.main -s "$station" --limit 10 > "data_$station.txt"
done
```

### Cas 2: Monitoring en temps réel
```bash
watch -n 300 "python -m meteo_toulouse.main -s paul --limit 1"
```

### Cas 3: Intégration avec d'autres outils
```bash
python -m meteo_toulouse.main -s paul --limit 20 | grep "🌡️" | head -5
```

---

**Date**: Février 2026
**Version**: 2.0 (avec CLI)
**Status**: ✅ Prêt à l'emploi
