"""Application principale de récupération de données météorologiques.

Point d'entrée de l'application qui orchestrate:
1. Extraction des données via l'API
2. Traitement avec une file d'attente
3. Mappage vers objets métier
4. Stockage en liste chaînée
5. Affichage formaté

Peut être exécuté en mode interactif ou avec des arguments CLI:
- python -m meteo_toulouse.main                    # Mode interactif
- python -m meteo_toulouse.main --station toulouse # Station spécifique
- python -m meteo_toulouse.main --list             # Lister les stations
"""

import argparse
import sys
from meteo_toulouse.config import CONFIG
from meteo_toulouse.extractors.ApiDataExtractor import ApiDataExtractor
from meteo_toulouse.extractors.ExtractionQueue import ExtractionQueue, ExtractionTask
from meteo_toulouse.mappers.RecordMapper import RecordMapper
from meteo_toulouse.models.Station import Station
from meteo_toulouse.models.LinkedList import StationLinkedList


def parse_arguments() -> argparse.Namespace:
    """
    Parse les arguments de la ligne de commande.

    Returns:
        argparse.Namespace: Arguments parsés
    """
    parser = argparse.ArgumentParser(
        description="🌤️ Application Météo Toulouse - Récupère les données météorologiques en direct",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python -m meteo_toulouse.main                      # Mode interactif (par défaut)
  python -m meteo_toulouse.main --station paul       # Station: Paul Sabatier
  python -m meteo_toulouse.main -s paul              # Identique au dessus (raccourci)
  python -m meteo_toulouse.main --list               # Lister les stations disponibles
  python -m meteo_toulouse.main --limit 50           # Limiter le nombre de records (défaut: 100)
        """
    )

    parser.add_argument(
        '--station', '-s',
        type=str,
        help='Nom ou ID de la station météorologique',
        default=None
    )

    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='Afficher la liste des stations disponibles'
    )

    parser.add_argument(
        '--limit',
        type=int,
        help='Nombre maximum de records à afficher (défaut: 100)',
        default=100
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Mode verbeux avec plus de détails'
    )

    return parser.parse_args()


def get_available_stations() -> dict:
    """
    Retourne les stations disponibles.

    Returns:
        dict: Dictionnaire des stations avec leurs IDs et noms
    """
    return {station['id']: station['name'] for station in CONFIG['stations_cibles']}


def list_stations() -> None:
    """Affiche la liste des stations disponibles."""
    print()
    print("=" * 70)
    print("📍 STATIONS MÉTÉOROLOGIQUES DISPONIBLES")
    print("=" * 70)
    print()

    stations = get_available_stations()
    for station_id, station_name in stations.items():
        print(f"  ID: {station_id:3d} | Nom: {station_name}")

    print()
    print("Utilisation: python -m meteo_toulouse.main --station <nom>")
    print("             python -m meteo_toulouse.main -s <nom>")
    print()


def process_station_data(
    station_name: str,
    limit: int = 100,
    verbose: bool = False
) -> None:
    """
    Traite et affiche les données pour une station spécifique.

    Args:
        station_name (str): Nom de la station
        limit (int): Nombre de records à récupérer
        verbose (bool): Mode verbeux
    """
    print()
    print("=" * 70)
    print(f"🌤️  Application Météo Toulouse - Station: {station_name}")
    print("=" * 70)
    print()

    # Initialiser les composants
    extractor = ApiDataExtractor()
    mapper = RecordMapper()

    # Créer et traiter la file d'attente
    extraction_queue = ExtractionQueue()
    task = ExtractionTask(source_type="api", target_name=station_name)
    extraction_queue.enqueue(task)

    if verbose:
        print(f"📋 Station: {station_name}")
        print(f"📊 Limite de records: {limit}")
        print()

    # Extraire les données
    print("📥 Extraction des données...")
    raw_data_results = extraction_queue.process_queue(extractor)
    print()

    # Traiter et afficher
    station_linked_list = StationLinkedList()

    for name, raw_data in raw_data_results.items():
        station = Station(nom=name)

        if raw_data and "results" in raw_data:
            records = raw_data.get("results", [])[:limit]
            print(f"✅ {name}: {len(records)} record(s) trouvé(s)")
            print()

            for record_data in records:
                record = mapper.to_object(record_data)
                station.add_record(record)
        else:
            print(f"⚠️  {name}: Aucune donnée trouvée")
            print()

        station_linked_list.append(station)

    # Afficher les résultats
    station_linked_list.display_all()

    print()
    print("=" * 70)
    print("✅ Application terminée")
    print("=" * 70)
    print()


def main_interactive() -> None:
    """
    Mode interactif: demande à l'utilisateur de sélectionner une station.
    """
    print()
    print("=" * 70)
    print("🌤️  Application Météo Toulouse (MODE INTERACTIF)")
    print("=" * 70)
    print()

    # Afficher les stations disponibles
    stations = get_available_stations()
    print("📍 Stations disponibles:")
    for station_id, station_name in stations.items():
        print(f"  {station_id}: {station_name}")
    print()

    # Demander à l'utilisateur de choisir
    while True:
        try:
            station_input = input("Choisissez une station (ID ou nom, ou 'q' pour quitter): ").strip()

            if station_input.lower() == 'q':
                print("👋 Au revoir!")
                sys.exit(0)

            # Vérifier si c'est un ID valide
            if station_input.isdigit():
                station_id = int(station_input)
                if station_id in stations:
                    station_name = stations[station_id]
                    break
                else:
                    print(f"❌ ID {station_id} non trouvé. Réessayez.")
            else:
                # Vérifier si c'est un nom
                found = False
                for station_id, station_name in stations.items():
                    if station_input.lower() in station_name.lower():
                        found = True
                        break

                if found:
                    break
                else:
                    print(f"❌ Station '{station_input}' non trouvée. Réessayez.")

        except KeyboardInterrupt:
            print("\n👋 Au revoir!")
            sys.exit(0)

    # Demander la limite de records
    while True:
        try:
            limit_str = input("Nombre de records à afficher (défaut: 100, max: 100): ").strip()
            if not limit_str:
                limit = 100
            else:
                limit = int(limit_str)
                if limit > 100:
                    print("⚠️  Maximum 100 records. Utilisation de 100.")
                    limit = 100
                elif limit <= 0:
                    print("⚠️  Doit être supérieur à 0. Utilisation de 100.")
                    limit = 100
            break
        except ValueError:
            print("❌ Veuillez entrer un nombre valide.")

    print()
    process_station_data(station_name, limit=limit, verbose=True)


def main() -> None:
    """
    Fonction principale - gère les arguments CLI ou mode interactif.

    Utilisation:
        python -m meteo_toulouse.main                    # Mode interactif
        python -m meteo_toulouse.main --station toulouse # Station spécifique
        python -m meteo_toulouse.main --list             # Lister les stations
    """
    args = parse_arguments()

    # Mode liste
    if args.list:
        list_stations()
        return

    # Mode avec station spécifiée
    if args.station:
        process_station_data(args.station, limit=args.limit, verbose=args.verbose)
        return

    # Mode interactif par défaut
    main_interactive()


if __name__ == "__main__":
    main()