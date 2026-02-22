"""Extracteur de données météorologiques depuis une API.

Ce module contient l'implémentation concrète de IDataExtractor
pour extraire les données depuis l'API OpenData Toulouse.
"""

from typing import Dict, Any
import requests
from meteo_toulouse.src.core.interfaces.IDataExtractor import IDataExtractor
from meteo_toulouse.src.core.utils.Configuration import Configuration


class ApiDataExtractor(IDataExtractor):
    """
    Extracteur de données depuis l'API OpenData Toulouse.

    Implémente l'interface IDataExtractor pour récupérer les données
    météorologiques depuis l'API officielle de Toulouse Métropole.

    Methods:
        extract(station_name: str) -> Dict[str, Any]: Extrait les données
                                                      pour une station
    """

    def extract(self, station_name: str) -> Dict[str, Any]:
        """
        Extrait les données météo pour une station depuis l'API.

        Args:
            station_name (str): Nom de la station cible

        Returns:
            Dict[str, Any]: Réponse JSON parsée de l'API contenant
                          les données météorologiques

        Raises:
            requests.exceptions.RequestException: Si la requête API échoue
            requests.exceptions.HTTPError: Si le code HTTP est en erreur
        """
        url = Configuration.get_station_url(station_name)
        print(f"📡 Requête API envoyée : {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
