from abc import ABC, abstractmethod

class IDataMapper(ABC):

    @abstractmethod
    def to_object(self, data: dict) -> object:

        pass
