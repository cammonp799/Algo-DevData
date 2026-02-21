"""Configuration des stations de métro de Toulouse avec données météo.

Le métro de Toulouse (Métro Ligne A et B) dessert les principales zones.
Voici la configuration avec les stations météo correspondant à chaque zone.
"""

# Stations de métro de Toulouse avec station météo la plus proche
METRO_STATIONS_CONFIG = {
    "ligne_a": [
        {
            "name": "Basso Cambo",
            "metro_line": "Ligne A",
            "weather_station": "Basso Cambo",
            "weather_id": 8,
            "description": "Station terminus ouest"
        },
        {
            "name": "Argoulets",
            "metro_line": "Ligne A",
            "weather_station": "La Salade",
            "weather_id": 9,
            "description": ""
        },
        {
            "name": "Bourdette",
            "metro_line": "Ligne A",
            "weather_station": "Soupetard",
            "weather_id": 11,
            "description": ""
        },
        {
            "name": "Jean Jaurès",
            "metro_line": "Ligne A",
            "weather_station": "Marengo",
            "weather_id": 2,
            "description": "Station centrale"
        },
        {
            "name": "Capitole",
            "metro_line": "Ligne A",
            "weather_station": "Carmes",
            "weather_id": 28,
            "description": "Station centre-ville"
        },
        {
            "name": "François Verdier",
            "metro_line": "Ligne A",
            "weather_station": "Reynerie",
            "weather_id": 26,
            "description": ""
        },
        {
            "name": "Palais de Justice",
            "metro_line": "Ligne A",
            "weather_station": "Île Empalot",
            "weather_id": 4,
            "description": ""
        },
        {
            "name": "Saint Agne",
            "metro_line": "Ligne A",
            "weather_station": "Île Empalot",
            "weather_id": 4,
            "description": ""
        },
        {
            "name": "Bellefontaine",
            "metro_line": "Ligne A",
            "weather_station": "Purpan",
            "weather_id": 36,
            "description": ""
        },
        {
            "name": "Mirail-Université",
            "metro_line": "Ligne A",
            "weather_station": "Paul Sabatier",
            "weather_id": 37,
            "description": "Terminus sud-est"
        },
    ],
    "ligne_b": [
        {
            "name": "Ramonville-Saint Agne",
            "metro_line": "Ligne B",
            "weather_station": "Île Empalot",
            "weather_id": 4,
            "description": "Station terminus sud"
        },
        {
            "name": "Pouvourville",
            "metro_line": "Ligne B",
            "weather_station": "Côte Pavé",
            "weather_id": 49,
            "description": ""
        },
        {
            "name": "Muret-Université",
            "metro_line": "Ligne B",
            "weather_station": "Paul Sabatier",
            "weather_id": 37,
            "description": ""
        },
        {
            "name": "Palais de Justice",
            "metro_line": "Ligne B",
            "weather_station": "Île Empalot",
            "weather_id": 4,
            "description": "Connexion avec Ligne A"
        },
        {
            "name": "Esquirol",
            "metro_line": "Ligne B",
            "weather_station": "Carmes",
            "weather_id": 28,
            "description": ""
        },
        {
            "name": "Jean Jaurès",
            "metro_line": "Ligne B",
            "weather_station": "Marengo",
            "weather_id": 2,
            "description": "Connexion avec Ligne A"
        },
        {
            "name": "Compans-Caffarelli",
            "metro_line": "Ligne B",
            "weather_station": "Parc Compans Cafarelli",
            "weather_id": 42,
            "description": ""
        },
        {
            "name": "Montaudran",
            "metro_line": "Ligne B",
            "weather_station": "Montaudran",
            "weather_id": 12,
            "description": ""
        },
        {
            "name": "Trois Cocus",
            "metro_line": "Ligne B",
            "weather_station": "Montaudran",
            "weather_id": 12,
            "description": ""
        },
        {
            "name": "Patte d'Oie",
            "metro_line": "Ligne B",
            "weather_station": "Purpan",
            "weather_id": 36,
            "description": ""
        },
        {
            "name": "Médipôle Tolosane",
            "metro_line": "Ligne B",
            "weather_station": "Purpan",
            "weather_id": 36,
            "description": ""
        },
        {
            "name": "Soupetard",
            "metro_line": "Ligne B",
            "weather_station": "Soupetard",
            "weather_id": 11,
            "description": ""
        },
        {
            "name": "Cépière",
            "metro_line": "Ligne B",
            "weather_station": "Soupetard",
            "weather_id": 11,
            "description": ""
        },
        {
            "name": "Hairabelle",
            "metro_line": "Ligne B",
            "weather_station": "Basso Cambo",
            "weather_id": 8,
            "description": "Terminus nord"
        },
    ]
}

# Liste des IDs météo (uniques) à interroger
STATIONS_CIBLES = sorted(
    {station["weather_id"] for stations in METRO_STATIONS_CONFIG.values() for station in stations}
)


if __name__ == "__main__":
    print("🚇 STATIONS DE MÉTRO DE TOULOUSE")
    print()
    print("LIGNE A:")
    for station in METRO_STATIONS_CONFIG["ligne_a"]:
        print(f"  • {station['name']:30} → Météo: {station['weather_station']}")
    print()
    print("LIGNE B:")
    for station in METRO_STATIONS_CONFIG["ligne_b"]:
        print(f"  • {station['name']:30} → Météo: {station['weather_station']}")
