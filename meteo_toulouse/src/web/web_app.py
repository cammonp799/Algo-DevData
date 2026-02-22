"""
Application Web Flask pour Météo Toulouse
Mode : Recherche par Station de Métro + MULTITHREADING
"""

import sys
import os
import concurrent.futures

# --- CONFIGURATION DU CHEMIN (PATH) ---
# On remonte de 3 dossiers (web -> src -> meteo_toulouse -> racine)
# pour que Python trouve bien le module 'meteo_toulouse'
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from flask import Flask, render_template, jsonify

# --- IMPORTATIONS (Avec la nouvelle architecture) ---
from meteo_toulouse.src.core.extractors.ApiDataExtractor import ApiDataExtractor
from meteo_toulouse.src.core.extractors.ExtractionQueue import ExtractionQueue, ExtractionTask
from meteo_toulouse.src.core.mappers.RecordMapper import RecordMapper
from meteo_toulouse.src.config.config import CONFIG
from meteo_toulouse.src.config.metro_stations_config import METRO_STATIONS_CONFIG, STATIONS_CIBLES

# --- INITIALISATION DE FLASK ---
# On dit explicitement à Flask où se trouvent 'templates' et 'static'
# par rapport à l'emplacement actuel de web_app.py
current_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    template_folder=os.path.join(current_dir, 'templates'),
    static_folder=os.path.join(current_dir, 'static')
)

# Création des index pour naviguer facilement entre les IDs, Noms et Datasets
STATION_NAMES = {str(s["id"]): s["name"] for s in CONFIG["stations_cibles"]}
ID_TO_DATASET = {str(s["id"]): s["dataset"] for s in CONFIG["stations_cibles"]}
DATASET_TO_ID = {s["dataset"]: str(s["id"]) for s in CONFIG["stations_cibles"]}


def fetch_station(task):
    """Fonction exécutée par chaque Thread pour récupérer UNE station."""
    extractor = ApiDataExtractor()
    mapper = RecordMapper()

    dataset_name = task.target_name
    station_id_str = DATASET_TO_ID.get(dataset_name)
    vrai_nom = STATION_NAMES.get(station_id_str, f"Station {station_id_str}")

    try:
        raw_data = extractor.extract(dataset_name)
        if raw_data and "results" in raw_data:
            records = [mapper.to_object(r) for r in raw_data["results"]]
            if records:
                latest_record = records[0]
                return station_id_str, {
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
    return station_id_str, None


def get_weather_data():
    """Récupère les données météo via un Pool de Threads."""
    stations_data = {}
    queue = ExtractionQueue()

    # 1. On remplit la file d'attente
    for station_id in STATIONS_CIBLES:
        dataset_name = ID_TO_DATASET.get(str(station_id))
        if dataset_name:
            queue.enqueue(ExtractionTask(target_name=dataset_name, source_type="api"))

    tasks = []
    while not queue.is_empty():
        tasks.append(queue.dequeue())

    # 2. On exécute les tâches en parallèle (10 threads simultanés)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_station, task) for task in tasks]
        for future in concurrent.futures.as_completed(futures):
            station_id, data = future.result()
            if data:
                stations_data[station_id] = data

    return stations_data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/metro_data')
def api_metro_data():
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
    print("🚇 Serveur Météo Métro (Multithread) lancé sur http://localhost:5001")
    app.run(debug=True, host='0.0.0.0', port=5001)