"""Structure de données : Liste Chaînée.

Ce module implémente une liste chaînée de stations météorologiques,
permettant le stockage et la traversée séquentielle des stations.

Structure: Chaque nœud contient une station et pointe vers le nœud suivant.
"""

from typing import Optional
from meteo_toulouse.src.core.models.Station import Station


class Node:
    """
    Nœud de la liste chaînée.

    Un nœud contient une station et une référence au nœud suivant.

    Attributes:
        station (Station): La station stockée dans ce nœud
        next (Optional[Node]): Référence au nœud suivant ou None
    """

    def __init__(self, station: Station) -> None:
        """
        Initialise un nouveau nœud.

        Args:
            station (Station): La station à stocker dans ce nœud
        """
        self.station: Station = station
        self.next: Optional['Node'] = None


class StationLinkedList:
    """
    Liste chaînée de stations météorologiques.

    Implémentation d'une liste chaînée simple pour stocker et parcourir
    les stations. Chaque station est dans un nœud lié au suivant.

    Structure: head -> Node(station1) -> Node(station2) -> ... -> None

    Attributes:
        head (Optional[Node]): Référence au premier nœud de la liste

    Methods:
        append(station: Station) -> None: Ajoute une station en fin de liste
        display_all() -> None: Affiche toutes les stations du début à la fin
    """

    def __init__(self) -> None:
        """Initialise une liste chaînée vide."""
        self.head: Optional[Node] = None

    def append(self, station: Station) -> None:
        """
        Ajoute une station à la fin de la liste chaînée.

        Opération: O(n) où n est le nombre de stations

        Args:
            station (Station): La station à ajouter

        Raises:
            TypeError: Si station n'est pas une instance de Station
        """
        if not isinstance(station, Station):
            raise TypeError(f"Expected Station, got {type(station)}")

        new_node = Node(station)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display_all(self) -> None:
        """
        Affiche toutes les stations du début à la fin de la liste.

        Utilise le décorateur StationDisplayDecorator pour formater
        l'affichage de chaque station.

        Opération: O(n) où n est le nombre de stations
        """
        from meteo_toulouse.src.core.decorators.StationDisplayDecorator import (
            StationDisplayDecorator
        )

        print("\n--- Parcours de la Liste Chaînée des Stations ---")
        current = self.head
        while current:
            print(f" Traitement du nœud pour : {current.station.nom}")
            decorator = StationDisplayDecorator(current.station)
            decorator.show()
            current = current.next
            print("  (lien vers le suivant)")
        print("--- Fin de la liste ---")