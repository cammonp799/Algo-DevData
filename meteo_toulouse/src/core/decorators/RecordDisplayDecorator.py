"""Décorateur pour l'affichage d'enregistrements météo.

Ce module implémente le Design Pattern Decorator pour ajouter
des responsabilités d'affichage aux objets Record.
"""

from meteo_toulouse.src.core.models import Record


class RecordDisplayDecorator:
    """
    Décorateur pour l'affichage formaté d'un enregistrement météo.

    Implémente le pattern Decorator pour ajouter du formatage
    d'affichage sans modifier la classe Record.

    Attributes:
        record (Record): L'enregistrement à afficher

    Methods:
        show() -> None: Affiche l'enregistrement de manière formatée
    """

    def __init__(self, record: Record) -> None:
        """
        Initialise le décorateur avec un enregistrement.

        Args:
            record (Record): L'enregistrement à décorer
        """
        self.record = record

    def show(self) -> None:
        """
        Affiche l'enregistrement avec tous ses paramètres météo.

        Format: 🕒 heure | 🌡️ temp | 💧 humidité | ⬇️ pression |
                🌧️ pluie | 💨 vent
        """
        print(
            f"🕒 {self.record.heure_utc} | 🌡️ {self.record.temperature}°C | "
            f"💧 {self.record.humidite}% | ⬇️ {self.record.pression} hPa | "
            f"🌧️ {self.record.pluie or 0} mm | "
            f"💨 {self.record.force_vent_moyen or 0} km/h"
        )
