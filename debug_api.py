#!/usr/bin/env python3
"""Script de debug pour tester l'API OpenData Toulouse.

Ce script aide à trouver les bonnes stations et datasets disponibles.
"""

import requests
import json
from meteo_toulouse.utils.Configuration import Configuration

def test_api_connection():
    """Teste la connexion à l'API."""
    print("🔍 Test de connexion à l'API OpenData Toulouse...")
    print()

    try:
        url = "https://data.toulouse-metropole.fr/api/records/1.0/search/?rows=1"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("✅ Connexion réussie à l'API")
        data = response.json()
        print(f"   Total records: {data.get('nhits', 'N/A')}")
        print()
    except Exception as e:
        print(f"❌ Erreur de connexion: {e}")
        return False

    return True


def list_available_datasets():
    """Liste tous les datasets contenant 'meteo' ou 'station'."""
    print("📚 Recherche des datasets météo disponibles...")
    print()

    try:
        # Chercher les datasets
        url = "https://data.toulouse-metropole.fr/api/datasets/1.0/search/?q=meteo&rows=50"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        datasets = data.get('datasets', [])

        if datasets:
            print(f"Trouvé {len(datasets)} dataset(s) contenant 'meteo':")
            print()
            for i, ds in enumerate(datasets[:10], 1):
                print(f"{i}. {ds.get('dataset_id', 'N/A')}")
                print(f"   Titre: {ds.get('metas', {}).get('title', 'N/A')}")
                print(f"   Records: {ds.get('records_count', 'N/A')}")
                print()
        else:
            print("⚠️  Aucun dataset trouvé")

    except Exception as e:
        print(f"❌ Erreur: {e}")


def test_station(station_name: str):
    """Teste la recherche pour une station spécifique."""
    print(f"🔍 Test de recherche pour: {station_name}")
    print()

    try:
        url = Configuration.get_station_url(station_name)
        print(f"URL: {url}")
        print()

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        nhits = data.get('nhits', 0)

        if nhits > 0:
            print(f"✅ Trouvé {nhits} record(s)!")
            records = data.get('records', [])

            if records:
                print()
                print("Premiers records:")
                for i, record in enumerate(records[:3], 1):
                    fields = record.get('fields', {})
                    print(f"  {i}. {fields.get('heure_utc', 'N/A')} - "
                          f"Temp: {fields.get('temperature', 'N/A')}°C")
        else:
            print(f"⚠️  Aucun record trouvé pour '{station_name}'")
            print()
            print("Essayez avec:")
            print("  - Toute la requête: ' ' pour voir tous les records")
            print("  - Un nom différent: 'airport', 'blagnac', etc.")

    except Exception as e:
        print(f"❌ Erreur: {e}")

    print()


def list_all_stations():
    """Liste les stations uniques disponibles."""
    print("📍 Recherche de toutes les stations disponibles...")
    print()

    try:
        # Chercher sans filtre pour voir tous les records
        url = (
            "https://data.toulouse-metropole.fr/api/records/1.0/search/"
            "?dataset=42-station-meteo-toulouse-parc-compans-cafarelli"
            "&rows=100"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        records = data.get('records', [])

        # Extraire les noms des stations
        stations = set()
        for record in records:
            fields = record.get('fields', {})
            nom_station = fields.get('nom_station', 'Inconnue')
            if nom_station:
                stations.add(nom_station)

        if stations:
            print(f"Trouvé {len(stations)} station(s):")
            for station in sorted(stations):
                print(f"  - {station}")
        else:
            print("⚠️  Aucune station trouvée")

    except Exception as e:
        print(f"❌ Erreur: {e}")

    print()


def main():
    """Fonction principale."""
    print("=" * 60)
    print("🌤️  DEBUG API OPENDATA TOULOUSE")
    print("=" * 60)
    print()

    # Test 1: Connexion
    if not test_api_connection():
        return

    # Test 2: Lister les stations
    list_all_stations()

    # Test 3: Tester différentes requêtes
    stations_to_test = [
        "toulouse",
        "station",
        "parc",
        "compans",
        "cafarelli",
        "blagnac",
        "francazal"
    ]

    print("🧪 Test de différentes requêtes:")
    print()

    for station in stations_to_test:
        test_station(station)

    print("=" * 60)
    print("✅ Debug terminé")
    print("=" * 60)


if __name__ == "__main__":
    main()
