#!/usr/bin/env python3
"""Script pour découvrir les stations météo disponibles sur OpenData Toulouse."""

import requests
import json

def discover_weather_stations():
    """Découvre toutes les stations météo disponibles."""

    print("=" * 70)
    print("🔍 DÉCOUVERTE DES STATIONS MÉTÉO DISPONIBLES")
    print("=" * 70)
    print()

    # Chercher les datasets contenant "meteo" ou "station"
    print("📊 Recherche des datasets météo...")

    try:
        # API pour lister les datasets
        url = "https://data.toulouse-metropole.fr/api/datasets/1.0/search/?q=meteo&rows=50"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            datasets = data.get('datasets', [])

            print(f"✅ Trouvé {len(datasets)} dataset(s) contenant 'meteo':\n")

            for i, dataset in enumerate(datasets, 1):
                dataset_id = dataset.get('dataset_id', 'N/A')
                title = dataset.get('metas', {}).get('title', 'N/A')
                records = dataset.get('records_count', 0)

                print(f"{i}. ID: {dataset_id}")
                print(f"   Titre: {title}")
                print(f"   Records: {records:,}")
                print()

            print("=" * 70)
            print("💡 INSTRUCTIONS POUR AJOUTER UNE STATION")
            print("=" * 70)
            print()
            print("1. Choisissez un dataset ID ci-dessus")
            print("2. Ouvrez meteo_toulouse/config.py")
            print("3. Ajoutez une station dans 'stations_cibles':")
            print()
            print('    {')
            print('        "id": NUMERO,')
            print('        "name": "Nom de la station",')
            print('        "dataset": "dataset-id-complet",')
            print('        "description": "Description"')
            print('    }')
            print()
            print("4. Testez avec:")
            print('   python -m meteo_toulouse.main --list')
            print('   python -m meteo_toulouse.main -s nom')

        else:
            print(f"❌ Erreur: {response.status_code}")

    except Exception as e:
        print(f"❌ Erreur: {e}")
        print()
        print("📌 Alternative: Visitez")
        print("   https://data.toulouse-metropole.fr/explore/")
        print("   Cherchez 'meteo' ou 'station'")


if __name__ == "__main__":
    discover_weather_stations()
