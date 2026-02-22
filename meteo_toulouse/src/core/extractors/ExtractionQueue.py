"""Structure de données : File d'Attente (Queue).

Ce module implémente une file d'attente FIFO (First-In-First-Out) pour
gérer les tâches d'extraction de données météorologiques.

Structure: [task1, task2, task3] - les tâches sont ajoutées à la fin
et retirées du début (FIFO).
"""

from typing import Optional, Dict, Any
from meteo_toulouse.src.core.interfaces.IDataExtractor import IDataExtractor


class ExtractionTask:
    """
    Représente une tâche d'extraction de données.

    Attributes:
        source_type (str): Type de source ('api', 'csv', 'json', etc.)
        target_name (str): Nom de la cible (station, fichier, etc.)
    """

    def __init__(self, source_type: str, target_name: str) -> None:
        """
        Initialise une tâche d'extraction.

        Args:
            source_type (str): Type de source de données
            target_name (str): Nom de la cible à extraire
        """
        self.source_type: str = source_type
        self.target_name: str = target_name


class ExtractionQueue:
    """
    File d'attente pour les tâches d'extraction (FIFO).

    Implémentation d'une file d'attente simple qui traite les tâches
    dans l'ordre FIFO (First-In-First-Out). Les tâches sont ajoutées
    à la fin et retirées du début.

    Structure interne: [tâche1, tâche2, tâche3] (tâche1 sera retirée en premier)

    Attributes:
        _queue (list): Liste interne stockant les tâches

    Methods:
        enqueue(task: ExtractionTask) -> None: Ajoute une tâche
        dequeue() -> Optional[ExtractionTask]: Retire et retourne la première tâche
        is_empty() -> bool: Vérifie si la file est vide
        process_queue(extractor_instance) -> Dict[str, Any]: Traite toute la file
    """

    def __init__(self) -> None:
        """Initialise une file d'attente vide."""
        self._queue: list = []

    def enqueue(self, task: ExtractionTask) -> None:
        """
        Ajoute une tâche à la fin de la file (opération O(1)).

        Args:
            task (ExtractionTask): La tâche à ajouter

        Raises:
            TypeError: Si task n'est pas une instance d'ExtractionTask
        """
        if not isinstance(task, ExtractionTask):
            raise TypeError(f"Expected ExtractionTask, got {type(task)}")
        self._queue.append(task)

    def dequeue(self) -> Optional[ExtractionTask]:
        """
        Retire et retourne la première tâche (opération O(n) - non optimal).

        Note: L'utilisation de list.pop(0) a une complexité O(n).
        Pour une meilleure performance, utiliser collections.deque.

        Returns:
            ExtractionTask: La première tâche ou None si vide

        Raises:
            IndexError: Si la file est vide
        """
        if self.is_empty():
            return None
        return self._queue.pop(0)

    def is_empty(self) -> bool:
        """
        Vérifie si la file d'attente est vide.

        Returns:
            bool: True si la file est vide, False sinon
        """
        return len(self._queue) == 0

    def process_queue(
        self, extractor_instance: IDataExtractor
    ) -> Dict[str, Any]:
        """
        Traite toutes les tâches de la file avec un extracteur.

        Retire les tâches une par une de la file et les traite
        avec l'extracteur fourni jusqu'à ce que la file soit vide.

        Args:
            extractor_instance (IDataExtractor): Instance de l'extracteur
                                                 à utiliser pour traiter

        Returns:
            Dict[str, Any]: Dictionnaire {nom_cible: données_extraites}

        Raises:
            ValueError: Si le type de source n'est pas supporté
        """
        results: Dict[str, Any] = {}
        while not self.is_empty():
            task = self.dequeue()
            print(
                f"📥 [FILE] Traitement de l'extraction : "
                f"{task.target_name} ({task.source_type})"
            )

            # Ici on pourrait switcher d'extracteur selon task.source_type
            if task.source_type == 'api':
                data = extractor_instance.extract(task.target_name)
                results[task.target_name] = data
            else:
                msg = (
                    f"⚠️ Type de source '{task.source_type}' "
                    f"non supporté pour le moment."
                )
                print(msg)

        return results