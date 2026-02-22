"""Tests unitaires pour les extracteurs et la file d'attente.

Tests pour:
- ExtractionTask: représentation d'une tâche
- ExtractionQueue: file d'attente FIFO
"""

import unittest
from meteo_toulouse.src.core.extractors.ExtractionQueue import (
    ExtractionQueue,
    ExtractionTask
)


class TestExtractionTask(unittest.TestCase):
    """Tests pour la classe ExtractionTask."""

    def test_task_creation(self):
        """Vérifie qu'une tâche est créée correctement."""
        task = ExtractionTask(source_type="api", target_name="toulouse-blagnac")
        self.assertEqual(task.source_type, "api")
        self.assertEqual(task.target_name, "toulouse-blagnac")

    def test_task_attributes(self):
        """Vérifie les attributs d'une tâche."""
        task = ExtractionTask(source_type="csv", target_name="file.csv")
        self.assertTrue(hasattr(task, 'source_type'))
        self.assertTrue(hasattr(task, 'target_name'))


class TestExtractionQueue(unittest.TestCase):
    """Tests pour la classe ExtractionQueue."""

    def setUp(self):
        """Initialisation avant chaque test."""
        self.queue = ExtractionQueue()
        self.task1 = ExtractionTask(
            source_type="api",
            target_name="toulouse-blagnac"
        )
        self.task2 = ExtractionTask(
            source_type="api",
            target_name="toulouse-francazal"
        )
        self.task3 = ExtractionTask(
            source_type="api",
            target_name="toulouse-pech-david"
        )

    def test_empty_queue(self):
        """Vérifie qu'une queue vide est reconnue."""
        self.assertTrue(self.queue.is_empty())

    def test_enqueue_single_task(self):
        """Vérifie l'ajout d'une tâche."""
        self.queue.enqueue(self.task1)
        self.assertFalse(self.queue.is_empty())

    def test_enqueue_multiple_tasks(self):
        """Vérifie l'ajout de plusieurs tâches."""
        self.queue.enqueue(self.task1)
        self.queue.enqueue(self.task2)
        self.queue.enqueue(self.task3)
        self.assertFalse(self.queue.is_empty())

    def test_dequeue_fifo_order(self):
        """Vérifie l'ordre FIFO du déqueuing."""
        self.queue.enqueue(self.task1)
        self.queue.enqueue(self.task2)
        self.queue.enqueue(self.task3)

        # Vérifier FIFO
        dequeued1 = self.queue.dequeue()
        self.assertEqual(dequeued1.target_name, "toulouse-blagnac")

        dequeued2 = self.queue.dequeue()
        self.assertEqual(dequeued2.target_name, "toulouse-francazal")

        dequeued3 = self.queue.dequeue()
        self.assertEqual(dequeued3.target_name, "toulouse-pech-david")

    def test_dequeue_empty_queue(self):
        """Vérifie le déqueuing d'une queue vide."""
        result = self.queue.dequeue()
        self.assertIsNone(result)

    def test_queue_becomes_empty(self):
        """Vérifie que la queue devient vide après déqueuing complet."""
        self.queue.enqueue(self.task1)
        self.assertFalse(self.queue.is_empty())

        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_enqueue_invalid_task(self):
        """Vérifie qu'ajouter un objet invalide lève une exception."""
        with self.assertRaises(TypeError):
            self.queue.enqueue("not a task")

    def test_queue_fifo_stress(self):
        """Test de stress avec plusieurs tâches."""
        tasks = []
        for i in range(10):
            task = ExtractionTask(
                source_type="api",
                target_name=f"station-{i}"
            )
            tasks.append(task)
            self.queue.enqueue(task)

        for i, expected_task in enumerate(tasks):
            dequeued = self.queue.dequeue()
            self.assertEqual(
                dequeued.target_name,
                expected_task.target_name
            )

        self.assertTrue(self.queue.is_empty())


if __name__ == '__main__':
    unittest.main()
