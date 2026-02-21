#!/bin/bash

echo "🌤️  Application Météo Toulouse - MODE DÉMONSTRATION"
echo ""
echo "Cette version utilise des DONNÉES MOCKÉES pour démonstration"
echo "car l'API OpenData ne retourne pas de données en temps réel."
echo ""

cd /Users/juniorchimene/PycharmProjects/project_weather_toulouse

# Activer l'environnement virtuel
if [ -d ".venv1" ]; then
    source .venv1/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
fi

echo "🚀 Lancement avec données mockées..."
echo ""

python << 'PYTHON_CODE'
from meteo_toulouse.config import CONFIG
from meteo_toulouse.extractors.ApiDataExtractor import ApiDataExtractor
from meteo_toulouse.extractors.ExtractionQueue import ExtractionQueue, ExtractionTask
from meteo_toulouse.mappers.RecordMapper import RecordMapper
from meteo_toulouse.models.Station import Station
from meteo_toulouse.models.LinkedList import StationLinkedList


def get_mock_data(station_name: str) -> dict:
    """Retourne des données mockées pour la démonstration."""
    mock_data = {
        "toulouse-blagnac": {
            "nhits": 3,
            "records": [
                {
                    "fields": {
                        "heure_utc": "2026-02-20T12:00:00",
                        "temperature": 8.5,
                        "humidite": 72.0,
                        "pression": 1013.5,
                        "pluie": 0.0,
                        "pluie_intensite_max": 0.0,
                        "direction_du_vecteur_vent_moyen": 180.0,
                        "force_vecteur_vent_moyen": 5.2,
                        "direction_du_vecteur_de_rafale_de_vent_max": 185.0,
                        "force_rafale_max": 10.5,
                        "nom_station": "Toulouse-Blagnac"
                    }
                },
                {
                    "fields": {
                        "heure_utc": "2026-02-20T13:00:00",
                        "temperature": 9.2,
                        "humidite": 70.0,
                        "pression": 1013.2,
                        "pluie": 0.0,
                        "pluie_intensite_max": 0.0,
                        "direction_du_vecteur_vent_moyen": 185.0,
                        "force_vecteur_vent_moyen": 5.8,
                        "direction_du_vecteur_de_rafale_de_vent_max": 190.0,
                        "force_rafale_max": 11.2,
                        "nom_station": "Toulouse-Blagnac"
                    }
                }
            ]
        },
        "toulouse-francazal": {
            "nhits": 2,
            "records": [
                {
                    "fields": {
                        "heure_utc": "2026-02-20T12:00:00",
                        "temperature": 7.8,
                        "humidite": 75.0,
                        "pression": 1013.8,
                        "pluie": 0.2,
                        "pluie_intensite_max": 0.5,
                        "direction_du_vecteur_vent_moyen": 190.0,
                        "force_vecteur_vent_moyen": 4.5,
                        "direction_du_vecteur_de_rafale_de_vent_max": 195.0,
                        "force_rafale_max": 9.8,
                        "nom_station": "Toulouse-Francazal"
                    }
                },
                {
                    "fields": {
                        "heure_utc": "2026-02-20T13:00:00",
                        "temperature": 8.3,
                        "humidite": 74.0,
                        "pression": 1013.6,
                        "pluie": 0.1,
                        "pluie_intensite_max": 0.3,
                        "direction_du_vecteur_vent_moyen": 188.0,
                        "force_vecteur_vent_moyen": 4.8,
                        "direction_du_vecteur_de_rafale_de_vent_max": 193.0,
                        "force_rafale_max": 10.1,
                        "nom_station": "Toulouse-Francazal"
                    }
                }
            ]
        },
        "toulouse-pech-david": {
            "nhits": 2,
            "records": [
                {
                    "fields": {
                        "heure_utc": "2026-02-20T12:00:00",
                        "temperature": 8.1,
                        "humidite": 73.0,
                        "pression": 1013.3,
                        "pluie": 0.0,
                        "pluie_intensite_max": 0.0,
                        "direction_du_vecteur_vent_moyen": 175.0,
                        "force_vecteur_vent_moyen": 5.0,
                        "direction_du_vecteur_de_rafale_de_vent_max": 180.0,
                        "force_rafale_max": 10.0,
                        "nom_station": "Toulouse-Pech-David"
                    }
                },
                {
                    "fields": {
                        "heure_utc": "2026-02-20T13:00:00",
                        "temperature": 8.8,
                        "humidite": 71.0,
                        "pression": 1013.1,
                        "pluie": 0.0,
                        "pluie_intensite_max": 0.0,
                        "direction_du_vecteur_vent_moyen": 178.0,
                        "force_vecteur_vent_moyen": 5.3,
                        "direction_du_vecteur_de_rafale_de_vent_max": 183.0,
                        "force_rafale_max": 10.6,
                        "nom_station": "Toulouse-Pech-David"
                    }
                }
            ]
        }
    }

    return mock_data.get(station_name, {"nhits": 0, "records": []})


class MockApiDataExtractor(ApiDataExtractor):
    """Extracteur API mocké pour la démonstration."""

    def extract(self, station_name: str) -> dict:
        """Retourne des données mockées."""
        print(f"📡 (DONNÉES SIMULÉES) Extraction pour: {station_name}")
        return get_mock_data(station_name)


# Fonction principale
print("=" * 70)
print("🌤️  Application Météo Toulouse (DONNÉES MOCKÉES)")
print("=" * 70)
print()

extractor = MockApiDataExtractor()
mapper = RecordMapper()

extraction_queue = ExtractionQueue()

print(f"📋 Chargement de la file d'attente avec {len(CONFIG['stations_cibles'])} stations...")
for station_name in CONFIG["stations_cibles"]:
    task = ExtractionTask(source_type="api", target_name=station_name)
    extraction_queue.enqueue(task)

print()

raw_data_results = extraction_queue.process_queue(extractor)

print()

station_linked_list = StationLinkedList()

print("🏗️ Construction des objets et de la liste chaînée...")
for name, raw_data in raw_data_results.items():
    station = Station(nom=name)

    if raw_data and "records" in raw_data:
        for record_data in raw_data["records"]:
            record = mapper.to_object(record_data)
            station.add_record(record)

    station_linked_list.append(station)

print()

station_linked_list.display_all()

print()
print("=" * 70)
print("✅ Application terminée")
print("=" * 70)
PYTHON_CODE

echo ""
echo "✅ Exécution terminée"
