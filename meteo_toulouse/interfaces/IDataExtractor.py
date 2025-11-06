from abc import ABC, abstractmethod

class IDataExtractor(ABC):

    @abstractmethod
    def extract(self, station_name: str) -> dict:

        pass
