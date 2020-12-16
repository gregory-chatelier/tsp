from typing import Union
from .problem import TSP

class Gene(object):
    city : str

    def __init__(self, city : Union[str, "Gene"]) -> None:
        self.city = str(city)

    def __str__(self):
        return self.city

    def __eq__(self, other : "Gene") -> bool:
        return str(self) == str(other)

    def __ne__(self, other : "Gene") -> bool:
        return str(self) != str(other)

    def distance(self, gene : "Gene") -> int:
        return TSP.distance(self.city, gene.city)
