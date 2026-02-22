"""Interface pour les mappeurs de données.

Définit le contrat que tous les mappeurs doivent respecter.
"""

from abc import ABC, abstractmethod
from typing import Any


class IDataMapper(ABC):
    """
    Interface abstraite pour le mappage de données.

    Définit le contrat que tous les mappeurs doivent implémenter.
    Permet de supporter différentes stratégies de mappage.

    Methods:
        to_object(data: Any) -> object: Mappe un dict vers un objet
    """

    @abstractmethod
    def to_object(self, data: Any) -> object:
        """
        Mappe des données brutes vers un objet structuré.

        Args:
            data (Any): Données brutes à mapper

        Returns:
            object: Objet structuré résultant du mappage
        """
        pass
