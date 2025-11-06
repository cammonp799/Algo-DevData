from meteo_toulouse.models.Station import Station
from meteo_toulouse.decorators.RecordDisplayDecorator import RecordDisplayDecorator

class StationDisplayDecorator:

    def __init__(self, station: Station):
        self.station = station

    def show(self):
        print(f"\n=== 🌤️ Station météo : {self.station.nom} ===")
        if not self.station.records:
            print("⚠️ Aucune donnée disponible pour cette station.")
        else:
            for record in self.station.records:
                RecordDisplayDecorator(record).show()
