import requests
from meteo_toulouse.interfaces.IDataExtractor import IDataExtractor
from meteo_toulouse.utils.Configuration import Configuration

class ApiDataExtractor(IDataExtractor):

    def extract(self, station_name: str) -> dict:
        url = Configuration.get_station_url(station_name)
        print(f"📡 Requête API envoyée : {url}")
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
