"""
Application Web Flask pour Météo Toulouse
Mode : Recherche par Station de Métro
"""

from flask import Flask, render_template, jsonify
import sys
import os

# Ajouter le chemin du projet
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from meteo_toulouse.extractors.ApiDataExtractor import ApiDataExtractor
from meteo_toulouse.extractors.ExtractionQueue import ExtractionQueue, ExtractionTask
from meteo_toulouse.mappers.RecordMapper import RecordMapper
from meteo_toulouse.config import CONFIG
from metro_stations_config import METRO_STATIONS_CONFIG, STATIONS_CIBLES

app = Flask(__name__, template_folder='templates', static_folder='static')

# Création des index pour naviguer facilement entre les IDs, Noms et Datasets
STATION_NAMES = {str(s["id"]): s["name"] for s in CONFIG["stations_cibles"]}
ID_TO_DATASET = {str(s["id"]): s["dataset"] for s in CONFIG["stations_cibles"]}
DATASET_TO_ID = {s["dataset"]: str(s["id"]) for s in CONFIG["stations_cibles"]}


def get_weather_data():
    """Récupère les données météo de toutes les stations."""
    stations_data = {}

    queue = ExtractionQueue()
    extractor = ApiDataExtractor()
    mapper = RecordMapper()

    # ÉTAPE 1 : Ajouter les datasets (et non les IDs) à la file d'attente
    for station_id in STATIONS_CIBLES:
        dataset_name = ID_TO_DATASET.get(str(station_id))
        if dataset_name:
            task = ExtractionTask(target_name=dataset_name, source_type="api")
            queue.enqueue(task)

    # ÉTAPE 2 : Traiter les requêtes
    while not queue.is_empty():
        task = queue.dequeue()
        dataset_name = task.target_name

        # On retrouve l'ID à partir du dataset
        station_id_str = DATASET_TO_ID.get(dataset_name)
        vrai_nom = STATION_NAMES.get(station_id_str, f"Station {station_id_str}")

        try:
            # L'extracteur reçoit bien le nom complet du dataset cette fois !
            raw_data = extractor.extract(dataset_name)
            if raw_data and "results" in raw_data:
                records = [mapper.to_object(r) for r in raw_data["results"]]
                if records:
                    latest_record = records[0]
                    # On stocke avec l'ID comme clé pour le front
                    stations_data[station_id_str] = {
                        "id": station_id_str,
                        "weather_name": vrai_nom,
                        "temperature": getattr(latest_record, 'temperature', None),
                        "humidite": getattr(latest_record, 'humidite', None),
                        "pluie": getattr(latest_record, 'pluie', 0),
                        "vent": getattr(latest_record, 'force_vent_moyen', None),
                        "heure": str(getattr(latest_record, 'heure_utc', 'N/A'))
                    }
        except Exception as e:
            print(f"Erreur {vrai_nom}: {e}")

    return stations_data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/metro_data')
def api_metro_data():
    """Renvoie la configuration du métro et la météo actuelle."""
    weather = get_weather_data()

    metro_stations = []
    for ligne in METRO_STATIONS_CONFIG.values():
        for station in ligne:
            weather_id = str(station["weather_id"])
            if weather_id in weather:
                station_data = station.copy()
                station_data["live_weather"] = weather[weather_id]
                metro_stations.append(station_data)

    return jsonify({"stations": metro_stations})


if __name__ == '__main__':
    print("🚇 Serveur Météo Métro lancé sur http://localhost:5001")
    app.run(debug=True, host='0.0.0.0', port=5001)