#!/usr/bin/env python3
"""Script pour obtenir la météo d'une station de métro spécifique."""

import sys
from metro_stations_config import METRO_STATIONS_CONFIG
from meteo_toulouse.extractors.ApiDataExtractor import ApiDataExtractor
from meteo_toulouse.mappers.RecordMapper import RecordMapper
from meteo_toulouse.decorators.RecordDisplayDecorator import RecordDisplayDecorator


def get_metro_station_by_name(name):
    """Cherche une station de métro par nom."""
    name_lower = name.lower()

    # Chercher dans Ligne A
    for station in METRO_STATIONS_CONFIG["ligne_a"]:
        if name_lower in station["name"].lower():
            return station, "Ligne A"

    # Chercher dans Ligne B
    for station in METRO_STATIONS_CONFIG["ligne_b"]:
        if name_lower in station["name"].lower():
            return station, "Ligne B"

    return None, None


def display_metro_weather(metro_station_name):
    """Affiche la météo pour une station de métro."""

    # Chercher la station
    station, line = get_metro_station_by_name(metro_station_name)

    if not station:
        print()
        print("❌ Station de métro non trouvée!")
        print()
        print("Stations disponibles:")
        print()
        print("🔵 LIGNE A:")
        for s in METRO_STATIONS_CONFIG["ligne_a"]:
            print(f"  • {s['name']}")
        print()
        print("🔴 LIGNE B:")
        for s in METRO_STATIONS_CONFIG["ligne_b"]:
            print(f"  • {s['name']}")
        print()
        return False

    # Récupérer les données
    metro_name = station["name"]
    weather_station = station["weather_station"]
    weather_id = station["weather_id"]

    print()
    print("=" * 80)
    print(f"🚇 MÉTÉO - Station de métro: {metro_name} ({line})")
    print("=" * 80)
    print()
    print(f"📍 Localisation: {metro_name}")
    print(f"🌡️  Station météo proche: {weather_station}")
    print(f"📊 ID Station: {weather_id}")
    print()

    try:
        # Extraire les données
        extractor = ApiDataExtractor()
        mapper = RecordMapper()

        response = extractor.extract(weather_station)

        if response and "results" in response and response["results"]:
            records = response["results"]

            print(f"📈 Derniers {min(5, len(records))} relevés météorologiques:")
            print()

            for i, record_data in enumerate(records[:5], 1):
                print(f"{i}. ", end="")
                record = mapper.to_object(record_data)
                RecordDisplayDecorator(record).show()

            print()
            print("=" * 80)
            print(f"✅ Données pour {metro_name}")
            print("=" * 80)
            return True
        else:
            print("⚠️  Aucune donnée disponible pour cette station")
            print()
            return False

    except Exception as e:
        print(f"❌ Erreur lors de la récupération des données: {e}")
        print()
        return False


def main():
    """Fonction principale."""

    if len(sys.argv) > 1:
        # Mode ligne de commande
        station_name = " ".join(sys.argv[1:])
        display_metro_weather(station_name)
    else:
        # Mode interactif
        print()
        print("=" * 80)
        print("🚇 MÉTÉO DES STATIONS DE MÉTRO DE TOULOUSE")
        print("=" * 80)
        print()
        print("Stations disponibles:")
        print()
        print("🔵 LIGNE A: Basso Cambo, Argoulets, Bourdette, Jean Jaurès, Capitole,")
        print("           François Verdier, Palais de Justice, Saint Agne, Bellefontaine,")
        print("           Mirail-Université")
        print()
        print("🔴 LIGNE B: Ramonville-Saint Agne, Pouvourville, Muret-Université,")
        print("           Palais de Justice, Esquirol, Jean Jaurès, Compans-Caffarelli,")
        print("           Montaudran, Trois Cocus, Patte d'Oie, Médipôle Tolosane,")
        print("           Soupetard, Cépière, Hairabelle")
        print()

        while True:
            try:
                station_name = input("🚇 Tapez le nom d'une station (ou 'q' pour quitter): ").strip()

                if station_name.lower() == 'q':
                    print("👋 Au revoir!")
                    break

                if not station_name:
                    print("⚠️  Veuillez entrer un nom de station")
                    continue

                print()
                display_metro_weather(station_name)
                print()

            except KeyboardInterrupt:
                print("\n👋 Au revoir!")
                break
            except Exception as e:
                print(f"❌ Erreur: {e}")


if __name__ == "__main__":
    main()
