"""Décorateur pour l'affichage de stations.

Ce module implémente le Design Pattern Decorator pour ajouter
des responsabilités d'affichage aux objets Station.
"""

from meteo_toulouse.models.Station import Station
from meteo_toulouse.decorators.RecordDisplayDecorator import RecordDisplayDecorator


class StationDisplayDecorator:
    """
    Décorateur pour l'affichage formaté d'une station.

    Implémente le pattern Decorator pour ajouter du formatage
    d'affichage sans modifier la classe Station.

    Attributes:
        station (Station): La station à afficher

    Methods:
        show() -> None: Affiche la station et ses enregistrements
    """

    def __init__(self, station: Station) -> None:
        """
        Initialise le décorateur avec une station.

        Args:
            station (Station): La station à décorer
        """
        self.station = station

    def show(self) -> None:
        """
        Affiche la station avec tous ses enregistrements.

        Parcourt tous les enregistrements de la station et les affiche
        en utilisant RecordDisplayDecorator pour le formatage.
        """
        print(f"\n=== 🌤️ Station météo : {self.station.nom} ===")
        if not self.station.records:
            print("⚠️ Aucune donnée disponible pour cette station.")
        else:
            for record in self.station.records:
                RecordDisplayDecorator(record).show()
