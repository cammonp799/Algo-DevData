"""Configuration centralisée de l'application.

Dictionnaire contenant tous les paramètres de configuration nécessaires
pour l'exécution de l'application.
"""

# Dictionnaire de configuration centralisé (Dictionary Pattern)
CONFIG = {
    # URL de base de l'API OpenData Toulouse
    "api_url_base": "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/",

    # TOUTES les stations météo de Toulouse et région
    "stations_cibles": [
        # ======== TOULOUSE CENTRE ========
        {"id": 37, "name": "Paul Sabatier", "dataset": "37-station-meteo-toulouse-universite-paul-sabatier"},
        {"id": 2, "name": "Marengo", "dataset": "02-station-mto-toulouse-marengo"},
        {"id": 3, "name": "Busca", "dataset": "03-station-mto-toulouse-busca"},
        {"id": 4, "name": "Ile Empalot", "dataset": "04-station-mto-toulouse-ile-empalot"},
        {"id": 5, "name": "Nakache", "dataset": "05-station-mto-toulouse-nakache"},
        {"id": 7, "name": "Avenue de Grande Bretagne", "dataset": "07-station-mto-toulouse-avenue-de-grande-bretagne"},
        {"id": 8, "name": "Basso Cambo", "dataset": "08-station-mto-toulouse-basso-cambo"},
        {"id": 9, "name": "La Salade", "dataset": "09-station-mto-toulouse-la-salade"},
        {"id": 11, "name": "Soupetard", "dataset": "11-station-mto-toulouse-soupetard"},
        {"id": 12, "name": "Montaudran", "dataset": "12-station-mto-toulouse-montaudran"},
        {"id": 13, "name": "Pech David", "dataset": "13-station-mto-toulouse-pech-david"},
        {"id": 14, "name": "Centre Pierre Potier", "dataset": "14-station-mto-toulouse-centre-pierre-potier"},
        {"id": 26, "name": "Reynerie", "dataset": "26-station-mto-toulouse-reynerie"},
        {"id": 28, "name": "Carmes", "dataset": "28-station-mto-toulouse-carmes"},
        {"id": 30, "name": "George Sand", "dataset": "30-station-mto-toulouse-george-sand"},
        {"id": 36, "name": "Purpan", "dataset": "36-station-mto-toulouse-purpan"},
        {"id": 38, "name": "Parc Jardin des Plantes", "dataset": "38-station-mto-toulouse-parc-jardin-des-plantes"},
        {"id": 40, "name": "ZI Thibaud", "dataset": "40-station-mto-toulouse-zi-thibaud"},
        {"id": 41, "name": "Avenue de Casselardit", "dataset": "41-station-mto-toulouse-avenue-de-casselardit"},
        {"id": 42, "name": "Parc Compans Cafarelli", "dataset": "42-station-mto-toulouse-parc-compans-cafarelli"},
        {"id": 44, "name": "Fondeyre", "dataset": "44-station-mto-toulouse-fondeyre"},
        {"id": 45, "name": "St Exupéry", "dataset": "45-station-mto-toulouse-st-exupery"},
        {"id": 48, "name": "La Machine AF", "dataset": "48-station-mto-toulouse-la-machine-af"},
        {"id": 49, "name": "Côte Pavé", "dataset": "49-station-mto-toulouse-cote-pave"},
        {"id": 50, "name": "Ponsan", "dataset": "50-station-mto-toulouse-ponsan"},
        {"id": 0, "name": "Valade", "dataset": "00-station-mto-toulouse-valade"},

        # ======== BANLIEUE PROCHE ========
        {"id": 15, "name": "L'Union", "dataset": "15-station-mto-lunion-ecole"},
        {"id": 16, "name": "Francazal", "dataset": "16-station-mto-toulouse-francazal"},
        {"id": 17, "name": "Fenouillet", "dataset": "17-station-mto-fenouillet-foyer"},
        {"id": 18, "name": "Brax", "dataset": "18-station-mto-brax-ecole"},
        {"id": 19, "name": "Mondouzil", "dataset": "19-station-mto-mondouzil-mairie"},
        {"id": 20, "name": "Mondonville", "dataset": "20-station-mto-mondonville-ecole"},
        {"id": 21, "name": "Cugnaux", "dataset": "21-station-mto-cugnaux-general-de-gaulle"},
        {"id": 22, "name": "Colomiers ZA Perget", "dataset": "22-station-mto-colomiers-za-perget"},
        {"id": 23, "name": "Pibrac", "dataset": "23-station-mto-pibrac-bouconne-centre-equestre"},
        {"id": 24, "name": "Colomiers ZI Enjacca", "dataset": "24-station-mto-colomiers-zi-enjacca"},
        {"id": 25, "name": "Tournefeuille Résidentiel", "dataset": "25-station-mto-tournefeuille-residentiel"},
        {"id": 31, "name": "Mons Station Epuration", "dataset": "31-station-mto-mons-station-puration"},
        {"id": 32, "name": "Mons École", "dataset": "32-station-mto-mons-ecole"},
        {"id": 33, "name": "Saint Jory", "dataset": "33-station-mto-saint-jory-chapelle-beldou"},
        {"id": 34, "name": "TESO", "dataset": "34-station-mto-toulouse-teso"},
        {"id": 39, "name": "Tournefeuille École", "dataset": "39-station-mto-tournefeuille-ecole"},
        {"id": 43, "name": "Balma", "dataset": "43-station-mto-balma-gramont"},
        {"id": 46, "name": "Blagnac", "dataset": "46-station-mto-blagnac-aéroport"},
        {"id": 47, "name": "La Machine TM", "dataset": "47-station-mto-toulouse-la-machine-tm"},
        {"id": 51, "name": "Blagnac Quinze Sols", "dataset": "53-station-mto-blagnac-quinze-sols"},
        {"id": 52, "name": "LIFE Gaston", "dataset": "65-station-mto-toulouse-life-gastou"},
        {"id": 53, "name": "LIFE Maréchal Juin", "dataset": "63-station-mto-toulouse-life-marchal-juin"},
        {"id": 54, "name": "LIFE Coubertin", "dataset": "66-station-mto-toulouse-life-coubertin"},
        {"id": 55, "name": "Parc Maourine", "dataset": "62-station-mto-toulouse-parc-maourine"},
    ],

    # Dataset par défaut
    "default_dataset": "37-station-meteo-toulouse-universite-paul-sabatier",

    # Mode d'extraction
    "extraction_mode": "api",

    # Nombre maximal de tentatives
    "max_retries": 3,

    # Nombre de records par requête
    "records_limit": 100
}