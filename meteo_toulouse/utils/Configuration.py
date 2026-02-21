"""Gestionnaire de configuration centralisé.

Ce module implémente le Design Pattern Singleton pour fournir
une configuration unique et accessible globalement.
"""

from typing import Optional


class Configuration:
    """
    Configuration centralisée (Singleton Pattern).

    Fournit une configuration unique pour toute l'application.
    Contient les paramètres essentiels pour l'accès à l'API.

    Attributes:
        BASE_URL (str): URL de base de l'API OpenData Toulouse
        DEFAULT_DATASET (str): Dataset par défaut contenant les stations

    Methods:
        get_station_url(station_id: int) -> str: Génère l'URL de requête
    """

    # URL de base de l'API OpenData Toulouse (v2.1)
    BASE_URL: str = "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/"

    # Dataset par défaut: Station Météo Toulouse - Université Paul Sabatier
    DEFAULT_DATASET: str = "37-station-meteo-toulouse-universite-paul-sabatier"

    @staticmethod
    def get_station_url(station_id: int = 37) -> Optional[str]:
        """
        Génère l'URL de requête pour une station donnée.

        Construit une URL formatée pour récupérer les données météo
        de la station météo de Toulouse.

        Args:
            station_id (int): ID de la station (défaut: 37 pour Paul Sabatier)

        Returns:
            str: URL formatée pour la requête API

        Example:
            >>> url = Configuration.get_station_url()
            >>> print(url)
            https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/...
        """
        return (
            f"{Configuration.BASE_URL}{Configuration.DEFAULT_DATASET}/records"
            f"?limit=100"
        )

    @staticmethod
    def get_all_datasets_url() -> str:
        """
        Génère l'URL pour lister tous les datasets disponibles.

        Returns:
            str: URL pour accéder à la liste des datasets
        """
        return f"{Configuration.BASE_URL}?limit=100"

