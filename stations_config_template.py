"""Stations météo pré-configurées pour Toulouse.

Vous pouvez utiliser cette configuration alternative dans config.py
si vous avez trouvé les dataset IDs correspondants.
"""

# Configuration avec PLUSIEURS stations (à utiliser si vous trouvez les IDs)
CONFIG_WITH_MULTIPLE_STATIONS = {
    "api_url_base": "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/",

    "stations_cibles": [
        {
            "id": 37,
            "name": "Paul Sabatier",
            "dataset": "37-station-meteo-toulouse-universite-paul-sabatier",
            "description": "Station Météo Toulouse - Université Paul Sabatier"
        },
        # Décommentez et complétez si vous trouvez les autres stations:
        # {
        #     "id": 42,
        #     "name": "Parc Compans",
        #     "dataset": "42-station-meteo-toulouse-parc-compans-cafarelli",
        #     "description": "Station Météo Toulouse - Parc Compans Caffarelli"
        # },
        # {
        #     "id": 1,
        #     "name": "Blagnac",
        #     "dataset": "blagnac-station-dataset",
        #     "description": "Station Météo Toulouse - Blagnac"
        # },
        # {
        #     "id": 2,
        #     "name": "Francazal",
        #     "dataset": "francazal-station-dataset",
        #     "description": "Station Météo Toulouse - Francazal"
        # },
        # {
        #     "id": 3,
        #     "name": "Pech-David",
        #     "dataset": "pech-david-station-dataset",
        #     "description": "Station Météo Toulouse - Pech-David"
        # },
    ],

    "default_dataset": "37-station-meteo-toulouse-universite-paul-sabatier",
    "extraction_mode": "api",
    "max_retries": 3,
    "records_limit": 100
}

if __name__ == "__main__":
    print("Stations pré-configurées:")
    print()
    for station in CONFIG_WITH_MULTIPLE_STATIONS["stations_cibles"]:
        print(f"✓ {station['name']:20} | ID: {station['id']:3} | {station['dataset']}")
    print()
    print("Pour ajouter d'autres stations:")
    print("1. Exécutez: python discover_stations.py")
    print("2. Trouvez le dataset ID pour chaque station")
    print("3. Décommentez et complétez les stations ci-dessus")
    print("4. Remplacez CONFIG dans meteo_toulouse/config.py")
