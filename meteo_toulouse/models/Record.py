from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Record:

    heure_utc: Optional[datetime]
    temperature: Optional[float]
    humidite: Optional[float]
    pression: Optional[float]
    pluie: Optional[float]
    pluie_intensite_max: Optional[float]
    direction_vent_moyen: Optional[float]
    force_vent_moyen: Optional[float]
    direction_rafale_max: Optional[float]
    force_rafale_max: Optional[float]
