"""Interface pour les extracteurs de données.

Définit le contrat que tous les extracteurs doivent respecter.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class IDataExtractor(ABC):
    """
    Interface abstraite pour l'extraction de données.

    Définit le contrat que tous les extracteurs doivent implémenter.
    Permet de supporter différentes sources (API, CSV, JSON, etc.).

    Methods:
        extract(station_name: str) -> Dict[str, Any]: Extrait les données
    """

    @abstractmethod
    def extract(self, station_name: str) -> Dict[str, Any]:
        """
        Extrait les données pour une station.

        Args:
            station_name (str): Nom de la station cible

        Returns:
            Dict[str, Any]: Données extraites au format spécifique
                          à l'implémentation
        """
        pass
