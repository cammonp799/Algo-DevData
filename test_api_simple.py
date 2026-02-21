#!/usr/bin/env python3
"""Script simple pour tester l'API et afficher les données."""

import requests

print("Testant l'API OpenData Toulouse...")
print()

# Tester l'accès de base
print("1️⃣  Test d'accès basique à l'API:")
url = "https://data.toulouse-metropole.fr/api/records/1.0/search/?rows=5"
response = requests.get(url, timeout=10)
if response.status_code == 200:
    data = response.json()
    print(f"✅ OK - Total records: {data.get('nhits', 0)}")
    print()
else:
    print(f"❌ Erreur: {response.status_code}")

# Lister les datasets disponibles
print("2️⃣  Cherchant les datasets 'meteo' ou 'station':")
url = "https://data.toulouse-metropole.fr/api/datasets/1.0/search/?q=meteo&rows=50"
response = requests.get(url, timeout=10)
if response.status_code == 200:
    data = response.json()
    datasets = data.get('datasets', [])
    if datasets:
        print(f"Trouvé {len(datasets)} datasets:")
        for ds in datasets[:5]:
            print(f"  - {ds.get('dataset_id', 'N/A')}")
    else:
        print("Aucun dataset trouvé")
print()

# Tester avec le dataset spécifié
print("3️⃣  Testant le dataset: 42-station-meteo-toulouse-parc-compans-cafarelli")
url = (
    "https://data.toulouse-metropole.fr/api/records/1.0/search/"
    "?dataset=42-station-meteo-toulouse-parc-compans-cafarelli"
    "&rows=10"
)
response = requests.get(url, timeout=10)
if response.status_code == 200:
    data = response.json()
    records = data.get('records', [])
    print(f"✅ Trouvé {data.get('nhits', 0)} records")

    if records:
        print()
        print("Noms de stations disponibles:")
        stations = set()
        for record in records:
            fields = record.get('fields', {})
            nom = fields.get('nom_station', 'N/A')
            if nom:
                stations.add(nom)

        for station in sorted(stations):
            print(f"  - {station}")
    else:
        print("⚠️  Aucun record retourné")
else:
    print(f"❌ Erreur: {response.status_code}")

print()
print("✅ Test terminé")
