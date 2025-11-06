from meteo_toulouse.models.Record import Record

class RecordDisplayDecorator:

    def __init__(self, record: Record):
        self.record = record

    def show(self):
        print(
            f"🕒 {self.record.heure_utc} | 🌡️ {self.record.temperature}°C | "
            f"💧 {self.record.humidite}% | ⬇️ {self.record.pression} hPa | "
            f"🌧️ {self.record.pluie or 0} mm | 💨 {self.record.force_vent_moyen or 0} km/h"
        )
