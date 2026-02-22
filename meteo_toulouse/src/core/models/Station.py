"""Modèle de données pour une station météorologique.

Ce module contient la classe Station représentant une station
météorologique avec ses enregistrements de données.
"""

from dataclasses import dataclass, field
from typing import List
from meteo_toulouse.src.core.models.Record import Record


@dataclass
class Station:
    """
    Station météorologique avec ses enregistrements.

    Cette classe représente une station météo unique et stocke
    tous les enregistrements associés.

    Attributes:
        nom (str): Nom/identifiant de la station
        records (List[Record]): Liste des enregistrements météo de la station

    Methods:
        add_record(record: Record) -> None: Ajoute un enregistrement à la station
    """

    nom: str
    records: List[Record] = field(default_factory=list)

    def add_record(self, record: Record) -> None:
        """
        Ajoute un enregistrement météo à la station.

        Args:
            record (Record): L'enregistrement à ajouter

        Raises:
            TypeError: Si record n'est pas une instance de Record
        """
        if not isinstance(record, Record):
            raise TypeError(f"Expected Record, got {type(record)}")
        self.records.append(record)
