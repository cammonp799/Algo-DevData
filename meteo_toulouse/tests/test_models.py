"""Tests unitaires pour les modèles de données.

Tests pour:
- Record: enregistrement météo
- Station: station météo
- LinkedList: liste chaînée de stations
"""

import unittest
from datetime import datetime
from meteo_toulouse.models.Record import Record
from meteo_toulouse.models.Station import Station
from meteo_toulouse.models.LinkedList import StationLinkedList, Node


class TestRecord(unittest.TestCase):
    """Tests pour la classe Record."""

    def setUp(self):
        """Initialisation avant chaque test."""
        self.record = Record(
            heure_utc=datetime(2025, 2, 20, 12, 30),
            temperature=8.5,
            humidite=72.0,
            pression=1013.0,
            pluie=0.0,
            pluie_intensite_max=0.0,
            direction_vent_moyen=180.0,
            force_vent_moyen=5.0,
            direction_rafale_max=180.0,
            force_rafale_max=10.0
        )

    def test_record_creation(self):
        """Vérifie qu'un Record est créé correctement."""
        self.assertEqual(self.record.temperature, 8.5)
        self.assertEqual(self.record.humidite, 72.0)

    def test_record_with_none_values(self):
        """Vérifie qu'un Record accepte les valeurs None."""
        record = Record(
            heure_utc=None,
            temperature=None,
            humidite=None,
            pression=None,
            pluie=None,
            pluie_intensite_max=None,
            direction_vent_moyen=None,
            force_vent_moyen=None,
            direction_rafale_max=None,
            force_rafale_max=None
        )
        self.assertIsNone(record.temperature)


class TestStation(unittest.TestCase):
    """Tests pour la classe Station."""

    def setUp(self):
        """Initialisation avant chaque test."""
        self.station = Station(nom="toulouse-blagnac")
        self.record = Record(
            heure_utc=datetime(2025, 2, 20, 12, 30),
            temperature=8.5,
            humidite=72.0,
            pression=1013.0,
            pluie=0.0,
            pluie_intensite_max=0.0,
            direction_vent_moyen=180.0,
            force_vent_moyen=5.0,
            direction_rafale_max=180.0,
            force_rafale_max=10.0
        )

    def test_station_creation(self):
        """Vérifie qu'une Station est créée correctement."""
        self.assertEqual(self.station.nom, "toulouse-blagnac")
        self.assertEqual(len(self.station.records), 0)

    def test_add_record(self):
        """Vérifie qu'un Record peut être ajouté à une Station."""
        self.station.add_record(self.record)
        self.assertEqual(len(self.station.records), 1)
        self.assertEqual(self.station.records[0].temperature, 8.5)

    def test_add_multiple_records(self):
        """Vérifie qu'on peut ajouter plusieurs Records."""
        self.station.add_record(self.record)
        record2 = Record(
            heure_utc=datetime(2025, 2, 20, 13, 30),
            temperature=9.0,
            humidite=75.0,
            pression=1012.0,
            pluie=0.0,
            pluie_intensite_max=0.0,
            direction_vent_moyen=180.0,
            force_vent_moyen=5.0,
            direction_rafale_max=180.0,
            force_rafale_max=10.0
        )
        self.station.add_record(record2)
        self.assertEqual(len(self.station.records), 2)

    def test_add_invalid_record(self):
        """Vérifie qu'ajouter un objet invalide lève une exception."""
        with self.assertRaises(TypeError):
            self.station.add_record("not a record")


class TestNode(unittest.TestCase):
    """Tests pour la classe Node."""

    def setUp(self):
        """Initialisation avant chaque test."""
        self.station = Station(nom="toulouse-blagnac")
        self.node = Node(self.station)

    def test_node_creation(self):
        """Vérifie qu'un Node est créé correctement."""
        self.assertEqual(self.node.station.nom, "toulouse-blagnac")
        self.assertIsNone(self.node.next)

    def test_node_link(self):
        """Vérifie qu'on peut lier deux nœuds."""
        station2 = Station(nom="toulouse-francazal")
        node2 = Node(station2)
        self.node.next = node2
        self.assertEqual(self.node.next.station.nom, "toulouse-francazal")


class TestLinkedList(unittest.TestCase):
    """Tests pour la classe StationLinkedList."""

    def setUp(self):
        """Initialisation avant chaque test."""
        self.linked_list = StationLinkedList()
        self.station1 = Station(nom="toulouse-blagnac")
        self.station2 = Station(nom="toulouse-francazal")
        self.station3 = Station(nom="toulouse-pech-david")

    def test_empty_list(self):
        """Vérifie qu'une liste vide a un head None."""
        self.assertIsNone(self.linked_list.head)

    def test_append_single_station(self):
        """Vérifie qu'on peut ajouter une station à une liste vide."""
        self.linked_list.append(self.station1)
        self.assertIsNotNone(self.linked_list.head)
        self.assertEqual(self.linked_list.head.station.nom, "toulouse-blagnac")
        self.assertIsNone(self.linked_list.head.next)

    def test_append_multiple_stations(self):
        """Vérifie qu'on peut ajouter plusieurs stations."""
        self.linked_list.append(self.station1)
        self.linked_list.append(self.station2)
        self.linked_list.append(self.station3)

        current = self.linked_list.head
        self.assertEqual(current.station.nom, "toulouse-blagnac")
        current = current.next
        self.assertEqual(current.station.nom, "toulouse-francazal")
        current = current.next
        self.assertEqual(current.station.nom, "toulouse-pech-david")
        self.assertIsNone(current.next)

    def test_append_invalid_station(self):
        """Vérifie qu'ajouter un objet invalide lève une exception."""
        with self.assertRaises(TypeError):
            self.linked_list.append("not a station")

    def test_list_order(self):
        """Vérifie que l'ordre d'ajout est préservé."""
        stations = ["station1", "station2", "station3"]
        for name in stations:
            self.linked_list.append(Station(nom=name))

        current = self.linked_list.head
        for expected_name in stations:
            self.assertEqual(current.station.nom, expected_name)
            current = current.next


if __name__ == '__main__':
    unittest.main()
