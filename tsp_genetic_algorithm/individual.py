import random
from .gene import Gene
from .problem import TSP
from .parameters import Parameters
from typing import List

class Individual(object):
    fitness : float = -1
    genome : List[Gene]

    def __init__(self, genome : List[Gene], mutate = False) -> None:
        self.genome = genome
        if mutate: self.mutate()

    @classmethod
    def construct_from_cities(cls) -> None:
        cities = TSP.cities[:]
        random.shuffle(cities)
        return cls(genome = [Gene(city) for city in cities])
    
    @classmethod
    def construct_from_father(cls, father : "Individual") -> None:
        return cls(genome = father.genome[:], mutate = True)

    @classmethod
    def construct_from_parents(cls, father : "Individual", mother : "Individual") -> None:
        cutting_point : int = random.randrange(0, len(father.genome))
        genome = father.genome[:cutting_point + 1]
        genome.extend([gene for gene in mother.genome if gene not in genome])
        return cls(genome, mutate = True)

    def mutate(self) -> None:
        if random.random() < Parameters.mutations_rate:
            index1 : int = random.randrange(0, len(self.genome))
            index2 : int = random.randrange(0, len(self.genome))
            self.genome[index1], self.genome[index2] = self.genome[index2], self.genome[index1]
    
    def evaluate(self) -> None:
        self.fitness = sum([gene2.distance(gene1) for gene1, gene2 in zip(self.genome[1:], self.genome[:-1])]) + self.genome[0].distance(self.genome[-1])
    
    def __str__(self):
        return f"{self.fitness} :" + " - ".join([str(gene) for gene in self.genome])
