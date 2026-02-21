#!/usr/bin/env python3
"""Affiche la météo pour chaque station de métro de Toulouse."""

from metro_stations_config import METRO_STATIONS_CONFIG
from meteo_toulouse.extractors.ApiDataExtractor import ApiDataExtractor
from meteo_toulouse.mappers.RecordMapper import RecordMapper
from meteo_toulouse.decorators.RecordDisplayDecorator import RecordDisplayDecorator
import time


def get_metro_weather():
    """Récupère et affiche la météo pour chaque station de métro."""

    extractor = ApiDataExtractor()
    mapper = RecordMapper()

    print("=" * 80)
    print("🚇 MÉTÉO DES STATIONS DE MÉTRO DE TOULOUSE")
    print("=" * 80)
    print()

    # Traiter Ligne A
    print("🔵 LIGNE A")
    print("-" * 80)
    print()

    weather_data_cached = {}

    for station in METRO_STATIONS_CONFIG["ligne_a"]:
        metro_name = station["name"]
        weather_station = station["weather_station"]
        weather_id = station["weather_id"]

        print(f"🚆 {metro_name:30} | Météo: {weather_station}")

        try:
            # Récupérer les données météo si pas déjà en cache
            if weather_id not in weather_data_cached:
                from meteo_toulouse.utils.Configuration import Configuration
                from meteo_toulouse.config import CONFIG

                # Chercher le dataset pour cette station
                for station_config in CONFIG["stations_cibles"]:
                    if station_config["id"] == weather_id:
                        dataset = station_config["dataset"]
                        url = f"https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/{dataset}/records?limit=1"
                        response = extractor.extract(weather_station)
                        weather_data_cached[weather_id] = response
                        break

                if weather_id not in weather_data_cached:
                    print(f"   ⚠️  Données non disponibles")
                    continue

            # Afficher le dernier enregistrement
            response = weather_data_cached[weather_id]
            if response and "results" in response and response["results"]:
                record_data = response["results"][0]  # Le plus récent
                record = mapper.to_object(record_data)
                print(f"   ", end="")
                RecordDisplayDecorator(record).show()
            else:
                print(f"   ⚠️  Aucune donnée disponible")

        except Exception as e:
            print(f"   ❌ Erreur: {str(e)[:50]}")

        print()

    # Traiter Ligne B
    print()
    print("🔴 LIGNE B")
    print("-" * 80)
    print()

    for station in METRO_STATIONS_CONFIG["ligne_b"]:
        metro_name = station["name"]
        weather_station = station["weather_station"]
        weather_id = station["weather_id"]

        print(f"🚆 {metro_name:30} | Météo: {weather_station}")

        try:
            # Récupérer les données météo si pas déjà en cache
            if weather_id not in weather_data_cached:
                from meteo_toulouse.utils.Configuration import Configuration
                from meteo_toulouse.config import CONFIG

                # Chercher le dataset pour cette station
                for station_config in CONFIG["stations_cibles"]:
                    if station_config["id"] == weather_id:
                        dataset = station_config["dataset"]
                        url = f"https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/{dataset}/records?limit=1"
                        response = extractor.extract(weather_station)
                        weather_data_cached[weather_id] = response
                        break

                if weather_id not in weather_data_cached:
                    print(f"   ⚠️  Données non disponibles")
                    continue

            # Afficher le dernier enregistrement
            response = weather_data_cached[weather_id]
            if response and "results" in response and response["results"]:
                record_data = response["results"][0]  # Le plus récent
                record = mapper.to_object(record_data)
                print(f"   ", end="")
                RecordDisplayDecorator(record).show()
            else:
                print(f"   ⚠️  Aucune donnée disponible")

        except Exception as e:
            print(f"   ❌ Erreur: {str(e)[:50]}")

        print()

    print("=" * 80)
    print("✅ Affichage terminé")
    print("=" * 80)


if __name__ == "__main__":
    get_metro_weather()
