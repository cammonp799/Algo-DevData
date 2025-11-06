from dataclasses import dataclass, field
from typing import List
from meteo_toulouse.models.Record import Record

@dataclass
class Station:

    nom: str
    records: List[Record] = field(default_factory=list)

    def add_record(self, record: Record):
        self.records.append(record)
