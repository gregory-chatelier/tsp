from typing import List

class TSP():
    cities : List[str] = [
            "Paris",
            "Lyon",
            "Marseille",
            "Nantes",
            "Bordeaux",
            "Toulouse",
            "Lille",
            ]
    distances : List[List[int]] = [
        [0, 462, 772, 379, 546, 678, 215],
        [462, 0, 326, 598, 842, 506, 664],
        [772, 326, 0, 909, 555, 407, 1005],
        [379, 598, 909, 0, 338, 540, 584],
        [546, 842, 555, 338, 0, 250, 792],
        [678, 506, 407, 540, 250, 0, 926],
        [215, 664, 1005, 584, 792, 926, 0],
        ]
    
    @classmethod
    def distance(cls, city1: str, city2: str) -> int:
        return cls.distances[cls.cities.index(city1)][cls.cities.index(city2)]
