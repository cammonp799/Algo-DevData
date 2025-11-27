class Node:

    def __init__(self, station):
        self.station = station
        self.next = None


class StationLinkedList:

    def __init__(self):
        self.head = None

    def append(self, station):
        new_node = Node(station)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display_all(self):
        from ..decorators.StationDisplayDecorator import StationDisplayDecorator

        print("\n--- Parcours de la Liste Chaînée des Stations ---")
        current = self.head
        while current:
            print(f" Traitement du nœud pour : {current.station.nom}")
            decorator = StationDisplayDecorator(current.station)
            decorator.show()
            current = current.next
            print("  (lien vers le suivant)")
        print("--- Fin de la liste ---")