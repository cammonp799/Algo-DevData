from meteo_toulouse.extractors.ApiDataExtractor import ApiDataExtractor
from meteo_toulouse.mappers.RecordMapper import RecordMapper
from meteo_toulouse.models.Station import Station
from meteo_toulouse.decorators.StationDisplayDecorator import StationDisplayDecorator

def main():
    print("=== 🌤️ Application Météo Toulouse ===")
    station_name = input("Entrez le nom de la station météo (ex: compans, blagnac, purpan...) : ")

    extractor = ApiDataExtractor()
    mapper = RecordMapper()

    # Extraction
    raw_data = extractor.extract(station_name)

    # Mapping vers objets Python
    station = Station(nom=station_name)
    for record_data in raw_data.get("records", []):
        record = mapper.to_object(record_data)
        station.add_record(record)

    # Affichage
    StationDisplayDecorator(station).show()

if __name__ == "__main__":
    main()
