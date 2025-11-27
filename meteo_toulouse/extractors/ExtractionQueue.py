from collections import deque


# On peut utiliser 'deque' de python qui est optimisé,
# ou implémenter une classe pure si c'est un exercice algorithmique.
# Voici une implémentation classe pure pour l'exercice :

class ExtractionTask:
    def __init__(self, source_type, target_name):
        self.source_type = source_type  # 'api', 'csv', etc.
        self.target_name = target_name


class ExtractionQueue:
    def __init__(self):
        self._queue = []

    def enqueue(self, task):
        """Ajoute une tâche d'extraction à la fin de la file."""
        self._queue.append(task)

    def dequeue(self):
        """Retire et retourne la prochaine tâche (FIFO)."""
        if self.is_empty():
            return None
        return self._queue.pop(0)

    def is_empty(self):
        return len(self._queue) == 0

    def process_queue(self, extractor_instance):
        """Traite toute la file avec l'extracteur fourni."""
        results = {}
        while not self.is_empty():
            task = self.dequeue()
            print(f"📥 [FILE] Traitement de l'extraction : {task.target_name} ({task.source_type})")

            # Ici on pourrait switcher d'extracteur selon task.source_type
            if task.source_type == 'api':
                data = extractor_instance.extract(task.target_name)
                results[task.target_name] = data
            else:
                print(f"⚠️ Type de source '{task.source_type}' non supporté pour le moment.")

        return results