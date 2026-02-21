"""Modèle de données pour un enregistrement météorologique.

Ce module contient la classe Record représentant un enregistrement
de données météorologiques d'une station.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Record:
    """
    Enregistrement des données météorologiques d'une station.

    Cette classe représente un relevé météo unique avec tous les
    paramètres mesurés par une station météorologique.

    Attributes:
        heure_utc (Optional[datetime]): Timestamp du relevé en UTC
        temperature (Optional[float]): Température en °C
        humidite (Optional[float]): Humidité relative en %
        pression (Optional[float]): Pression atmosphérique en hPa
        pluie (Optional[float]): Cumul de pluie en mm
        pluie_intensite_max (Optional[float]): Intensité max de pluie en mm/h
        direction_vent_moyen (Optional[float]): Direction moyenne du vent (0-360°)
        force_vent_moyen (Optional[float]): Force moyenne du vent en km/h
        direction_rafale_max (Optional[float]): Direction des rafales max (0-360°)
        force_rafale_max (Optional[float]): Force des rafales max en km/h
    """

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
