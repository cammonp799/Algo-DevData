from datetime import datetime
from meteo_toulouse.interfaces.IDataMapper import IDataMapper
from meteo_toulouse.models.Record import Record

class RecordMapper(IDataMapper):

    def to_object(self, data: dict) -> Record:
        fields = data.get("fields", {})
        return Record(
            heure_utc=self._parse_date(fields.get("heure_utc")),
            temperature=fields.get("temperature"),
            humidite=fields.get("humidite"),
            pression=fields.get("pression"),
            pluie=fields.get("pluie"),
            pluie_intensite_max=fields.get("pluie_intensite_max"),
            direction_vent_moyen=fields.get("direction_du_vecteur_vent_moyen"),
            force_vent_moyen=fields.get("force_vecteur_vent_moyen"),
            direction_rafale_max=fields.get("direction_du_vecteur_de_rafale_de_vent_max"),
            force_rafale_max=fields.get("force_rafale_max"),
        )

    def _parse_date(self, date_str: str):
        try:
            return datetime.fromisoformat(date_str)
        except Exception:
            return None
