"""
Application Web Flask pour Météo Toulouse
Frontend moderne pour visualiser les données météo en temps réel
"""


from flask import Flask, render_template, jsonify
import sys
import os

# Ajouter le chemin du projet
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from meteo_toulouse.extractors.ApiDataExtractor import ApiDataExtractor
from meteo_toulouse.extractors.ExtractionQueue import ExtractionQueue, ExtractionTask
from meteo_toulouse.mappers.RecordMapper import RecordMapper
from metro_stations_config import STATIONS_CIBLES

app = Flask(__name__, template_folder='templates', static_folder='static')


def get_weather_data():
    """Récupère les données météo de toutes les stations."""
    stations_data = []

    # Créer la file d'attente et l'extracteur
    queue = ExtractionQueue()
    extractor = ApiDataExtractor()
    mapper = RecordMapper()

    # Ajouter les stations à la file
    for station_id in STATIONS_CIBLES:
        task = ExtractionTask(station_id=station_id, source_type="api")
        queue.enqueue(task)

    # Traiter la file
    while not queue.is_empty():
        task = queue.dequeue()
        station_id = task.station_id

        try:
            raw_data = extractor.extract(station_id)
            if raw_data:
                records = mapper.map(raw_data)

                # Prendre le dernier enregistrement (le plus récent)
                if records:
                    latest_record = records[0] if isinstance(records, list) else records

                    station_info = {
                        "id": station_id,
                        "name": station_id.replace("-", " ").title(),
                        "temperature": getattr(latest_record, 'temperature', None),
                        "humidite": getattr(latest_record, 'humidite', None),
                        "pression": getattr(latest_record, 'pression', None),
                        "pluie": getattr(latest_record, 'pluie', 0),
                        "vent": getattr(latest_record, 'force_vent_moyen', None),
                        "direction_vent": getattr(latest_record, 'direction_vent_moyen', None),
                        "heure": str(getattr(latest_record, 'heure_utc', 'N/A'))
                    }
                    stations_data.append(station_info)
        except Exception as e:
            print(f"Erreur pour {station_id}: {e}")
            stations_data.append({
                "id": station_id,
                "name": station_id.replace("-", " ").title(),
                "error": str(e)
            })

    return stations_data


@app.route('/')
def index():
    """Page principale."""
    return render_template('index.html')


@app.route('/api/weather')
def api_weather():
    """API endpoint pour les données météo."""
    try:
        data = get_weather_data()
        return jsonify({"success": True, "stations": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route('/api/stations')
def api_stations():
    """Liste des stations disponibles."""
    return jsonify({"stations": list(STATIONS_CIBLES)})


if __name__ == '__main__':
    print("🌤️ Démarrage du serveur Météo Toulouse...")
    app.run(debug=True, host='0.0.0.0', port=5001)