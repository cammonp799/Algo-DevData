class Configuration:


    BASE_URL = "https://data.toulouse-metropole.fr/api/records/1.0/search/"
    DEFAULT_DATASET = "42-station-meteo-toulouse-parc-compans-cafarelli"

    @staticmethod
    def get_station_url(station_name: str) -> str:

        query = station_name.replace(" ", "+")
        return (
            f"{Configuration.BASE_URL}?dataset={Configuration.DEFAULT_DATASET}"
            f"&q={query}&rows=10&sort=-record_timestamp"
        )
