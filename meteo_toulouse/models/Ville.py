from dataclasses import dataclass, field
from typing import List
from meteo_toulouse.models.Station import Station


@dataclass
class Ville:

    nom: str
    stations: List[Station] = field(default_factory=list)

    def add_station(self, station: Station):
        self.stations.append(station)
