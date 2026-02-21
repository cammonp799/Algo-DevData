"""Mappeur de données brutes vers objets Record.

Ce module contient l'implémentation concrète de IDataMapper
pour transformer les données JSON brutes en objets Record.
"""

from datetime import datetime
from typing import Dict, Any, Optional
from meteo_toulouse.interfaces.IDataMapper import IDataMapper
from meteo_toulouse.models.Record import Record


class RecordMapper(IDataMapper):
    """
    Mappeur pour convertir des données JSON en objets Record.

    Implémente l'interface IDataMapper pour transformer les données
    brutes reçues de l'API en objets Record structurés.

    Ce pattern (Strategy Pattern) permet de changer facilement la
    logique de mappage ou d'ajouter de nouveaux mappeurs.

    Methods:
        to_object(data: Dict[str, Any]) -> Record: Convertit un dict en Record
        _parse_date(date_str: str) -> Optional[datetime]: Parse une date ISO
    """

    def to_object(self, data: Dict[str, Any]) -> Record:
        """
        Convertit un dictionnaire de données brutes en objet Record.

        Extrait les champs pertinents de la structure JSON de l'API
        et les mappe vers les attributs du Record.

        Structure attendue:
        {
            "heure_utc": "2022-01-10T05:15:00+00:00",
            "temperature_en_degre_c": 7.9,
            "humidite": 85,
            "pression": 94400,
            "pluie": 0,
            "pluie_intensite_max": 0,
            "direction_du_vecteur_vent_moyen": 146,
            "force_moyenne_du_vecteur_vent": 5,
            "direction_du_vecteur_de_vent_max": 14,
            "force_rafale_max": 11
        }

        Args:
            data (Dict[str, Any]): Dictionnaire contenant les données brutes

        Returns:
            Record: Objet Record initialisé avec les données mappées
        """
        return Record(
            heure_utc=self._parse_date(data.get("heure_utc")),
            temperature=data.get("temperature_en_degre_c"),
            humidite=data.get("humidite"),
            pression=data.get("pression"),
            pluie=data.get("pluie"),
            pluie_intensite_max=data.get("pluie_intensite_max"),
            direction_vent_moyen=data.get("direction_du_vecteur_vent_moyen"),
            force_vent_moyen=data.get("force_moyenne_du_vecteur_vent"),
            direction_rafale_max=data.get(
                "direction_du_vecteur_de_vent_max"
            ),
            force_rafale_max=data.get("force_rafale_max"),
        )

    @staticmethod
    def _parse_date(date_str: Optional[str]) -> Optional[datetime]:
        """
        Parse une chaîne de date au format ISO 8601.

        Convertit une chaîne de date au format ISO en objet datetime.
        Retourne None en cas d'erreur de parsing.

        Formats supportés:
        - "2022-01-10T05:15:00+00:00"
        - "2022-01-10T05:15:00Z"
        - "2022-01-10T05:15:00"

        Args:
            date_str (Optional[str]): Chaîne de date au format ISO

        Returns:
            Optional[datetime]: Objet datetime parsé ou None en cas d'erreur
        """
        if not date_str:
            return None
        try:
            # Gérer les formats avec timezone
            if date_str.endswith('Z'):
                date_str = date_str[:-1] + '+00:00'

            # Essayer de parser avec timezone
            try:
                return datetime.fromisoformat(date_str)
            except ValueError:
                # Si ça échoue, essayer sans timezone
                return datetime.fromisoformat(date_str.replace('+00:00', ''))
        except (ValueError, TypeError):
            return None
