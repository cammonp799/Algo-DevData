from .config import CONFIG
from .extractors.ApiDataExtractor import ApiDataExtractor
from .extractors.ExtractionQueue import ExtractionQueue, ExtractionTask
from .mappers.RecordMapper import RecordMapper
from .models.Station import Station
from .models.LinkedList import StationLinkedList


def main():
    print("=== 🌤️ Application Météo Toulouse (Structurée) ===")

    # 1. Initialisation des composants
    extractor = ApiDataExtractor()  # Utilise potentiellement CONFIG['api_url_base'] en interne si modifié
    mapper = RecordMapper()

    # 2. Utilisation de la FILE (Queue) pour préparer les extractions
    extraction_queue = ExtractionQueue()

    # On charge la file avec les stations définies dans la CONFIG
    print(f"📋 Chargement de la file d'attente avec {len(CONFIG['stations_cibles'])} stations...")
    for station_name in CONFIG["stations_cibles"]:
        task = ExtractionTask(source_type="api", target_name=station_name)
        extraction_queue.enqueue(task)

    # 3. Traitement de la file (Extraction des données)
    # Cela renvoie un dictionnaire { "nom_station": raw_data, ... }
    raw_data_results = extraction_queue.process_queue(extractor)

    # 4. Utilisation de la LISTE CHAÎNÉE pour stocker les objets Station
    station_linked_list = StationLinkedList()

    print("\n🏗️ Construction des objets et de la liste chaînée...")
    for name, raw_data in raw_data_results.items():
        # Création de l'objet Station
        station = Station(nom=name)

        # Mapping des données
        if raw_data and "records" in raw_data:
            for record_data in raw_data["records"]:
                record = mapper.to_object(record_data)
                station.add_record(record)

        # Ajout à la liste chaînée
        station_linked_list.append(station)

    # 5. Affichage via parcours de la liste chaînée
    station_linked_list.display_all()


if __name__ == "__main__":
    main()