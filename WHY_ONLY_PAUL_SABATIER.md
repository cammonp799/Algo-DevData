# ❓ POURQUOI SEUL PAUL SABATIER?

## 🎯 Réponse courte
Parce que c'est la seule station dont nous avons vérifié le dataset ID exact sur OpenData Toulouse.

## 📋 Explication détaillée

### Situation actuelle
- ✅ **1 station configurée**: Paul Sabatier (ID: 37)
- ✅ **180 000+ enregistrements** disponibles
- ✅ **Données réelles** depuis 2020

### Pourquoi pas d'autres?
L'API OpenData Toulouse a plusieurs datasets différents pour chaque station:
- Chaque station a son propre **dataset ID** unique
- Ces IDs doivent être découverts manuellement ou via l'API
- Nous avons configuré Paul Sabatier car nous l'avons testé

## 🚀 Comment ajouter d'autres stations?

### Option 1: Rapide (si vous connaissez les IDs)
```python
# Modifiez meteo_toulouse/config.py
"stations_cibles": [
    {"id": 37, "name": "Paul Sabatier", "dataset": "37-..."},
    {"id": 42, "name": "Parc Compans", "dataset": "42-..."},  # ← Ajoutez
    {"id": ?, "name": "Blagnac", "dataset": "?-..."},         # ← Ajoutez
]
```

### Option 2: Découverte (recommandé)
```bash
# Exécutez le script de découverte
python discover_stations.py
```

Cela affichera:
```
📊 Recherche des datasets météo...
✅ Trouvé 10 dataset(s) contenant 'meteo':

1. ID: 37-station-meteo-toulouse-universite-paul-sabatier
   Titre: Station Météo Toulouse - Université Paul Sabatier
   Records: 180,103

2. ID: 42-station-meteo-toulouse-parc-compans-cafarelli
   Titre: Station Météo Toulouse - Parc Compans Caffarelli
   Records: 50,000

3. ...
```

### Option 3: Site web OpenData
1. Visitez: https://data.toulouse-metropole.fr/explore/
2. Cherchez: "meteo" ou "station"
3. Notez les dataset IDs
4. Ajoutez-les dans config.py

## 📝 Exemple complet

### Avant (1 station)
```python
# meteo_toulouse/config.py
"stations_cibles": [
    {"id": 37, "name": "Paul Sabatier", "dataset": "37-station-meteo-toulouse-universite-paul-sabatier"}
]
```

```bash
$ python -m meteo_toulouse.main --list

📍 STATIONS MÉTÉOROLOGIQUES DISPONIBLES
  ID:  37 | Nom: Paul Sabatier
```

### Après (plusieurs stations)
```python
# meteo_toulouse/config.py
"stations_cibles": [
    {"id": 37, "name": "Paul Sabatier", "dataset": "37-station-meteo-toulouse-universite-paul-sabatier"},
    {"id": 42, "name": "Parc Compans", "dataset": "42-station-meteo-toulouse-parc-compans-cafarelli"},
    {"id": 1, "name": "Blagnac", "dataset": "1-station-meteo-toulouse-blagnac"},
]
```

```bash
$ python -m meteo_toulouse.main --list

📍 STATIONS MÉTÉOROLOGIQUES DISPONIBLES
  ID:  37 | Nom: Paul Sabatier
  ID:  42 | Nom: Parc Compans
  ID:   1 | Nom: Blagnac

$ python -m meteo_toulouse.main -s blagnac --limit 10
```

## 🔍 Pourquoi c'est comme ça?

### Raison technique
- OpenData Toulouse organise les données par **dataset**
- Chaque dataset a un **ID unique**
- Nous devons savoir cet ID pour accéder aux données
- Les IDs ne sont pas triviaux à deviner

### Raison pédagogique
- C'est un bon exemple de **configuration flexible**
- Vous apprenez à **ajouter des ressources**
- C'est **facile à étendre** sans modifier le code

## ✅ Checklist pour ajouter une station

- [ ] 1. Exécutez `python discover_stations.py`
- [ ] 2. Trouvez le dataset ID pour la station
- [ ] 3. Ouvrez `meteo_toulouse/config.py`
- [ ] 4. Ajoutez la station dans `stations_cibles`
- [ ] 5. Testez avec `python -m meteo_toulouse.main --list`
- [ ] 6. Testez avec `python -m meteo_toulouse.main -s nom`

## 💡 Aide-mémoire

```bash
# Découvrir les stations
python discover_stations.py

# Voir la liste configurée
python -m meteo_toulouse.main --list

# Tester une station
python -m meteo_toulouse.main -s paul --limit 5

# Chercher par mot-clé
python -m meteo_toulouse.main -s blagnac
python -m meteo_toulouse.main -s parc
python -m meteo_toulouse.main -s 42
```

## 🎯 Stations courantes à chercher

- [ ] Blagnac (Aéroport)
- [ ] Francazal (Aéroport)
- [ ] Pech-David
- [ ] Parc Compans
- [ ] Centre-ville
- [ ] Autres quartiers

## 📚 Ressources

- **OpenData Toulouse**: https://data.toulouse-metropole.fr/
- **Catalogue**: https://data.toulouse-metropole.fr/explore/
- **API Docs**: https://data.toulouse-metropole.fr/api/
- **Script**: `python discover_stations.py`
- **Guide**: `ADD_MORE_STATIONS.md`

## 🤔 Questions fréquentes

**Q: Peut-on ajouter une station sans relancer l'app?**  
R: Non, il faut modifier `config.py` et relancer l'app.

**Q: Combien de stations peut-on ajouter?**  
R: Autant qu'on veut! L'app scale facilement.

**Q: Comment supprimer Paul Sabatier?**  
R: Commentez ou supprimez sa ligne dans `config.py`.

**Q: Les données sont mises à jour?**  
R: Oui, en temps réel selon OpenData Toulouse.

---

**Vous êtes prêt!** 🚀

Exécutez:
```bash
python discover_stations.py
```

Puis modifiez `meteo_toulouse/config.py` pour ajouter d'autres stations!
