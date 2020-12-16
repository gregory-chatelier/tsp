import random
from .individual import Individual
from .parameters import Parameters
from typing import List

class EvolutionaryProcess(object):
    
    def __init__(self) -> None:
        # Population active : une liste d'individus
        self.population : List[Individual] = [Individual.construct_from_cities() for i in range(0, Parameters.individuals_nb)]
        # Numéro de la génération active
        self.generation_nb : int = 0
        # Meilleure valeur d'adaptation rencontrée jusqu'ici
        self.best_fitness : float = 0
        # Meilleur individu de la population active
        self.best_individual : Individual
        # Nouvelle génération d'individus à mixer à la population active 
        self.new_generation : List[Individual]

    def run(self) -> None:
        self.best_fitness = Parameters.min_fitness + 1
        while self.generation_nb < Parameters.generations_max_nb and self.best_fitness > Parameters.min_fitness:
            # Lance l'évaluation de chaque individus de la population
            self.evaluate(self.population)
            # Récupère le meilleur individu (la meilleure solution) et provoque son affichage
            self.best_individual = self.find_best_individual(self.population)
            print(f"Génération {self.generation_nb} -> {self.best_individual}")
            # Créé une population d'individus descendants de la population actuelle
            self.best_fitness = self.best_individual.fitness
            self.new_generation = self.generation(self.population)
            # Remplace la population par tout ou parti des descendants
            self.population = self.survival(self.new_generation)
            self.generation_nb += 1

    def evaluate(self, population) -> None:
        # Evaluate population
        for individual in population: individual.evaluate()

    def find_best_individual(self, population) -> Individual:
        # Find best individual
        return sorted(population, key=lambda e : e.fitness)[0]

    def generation(self, population) -> List[Individual]:
        # New generation
        new_generation = [self.best_individual] # Elitism
        for _ in range(Parameters.individuals_nb - 1):
            new_generation.append(self.reproduction(population))
        return new_generation

    def selection(self, population) -> Individual:
        # Sélection d'un individu dans la population pour en faire un parent
        # à l'aide d'un choix aléatoire sur une roulette biaisée sur le rang
        total_ranks : int = Parameters.individuals_nb * (Parameters.individuals_nb + 1) / 2
        rand : int = random.randrange(total_ranks)
        index : int = 0
        nb_parts : int = Parameters.individuals_nb
        total_parts : int = 0
        while total_parts < rand:
            index += 1
            total_parts += nb_parts
            nb_parts -= 1
        return sorted(population, key=lambda e : e.fitness)[index]

    def reproduction(self, population) -> Individual:
        father = self.selection(population)
        if random.random() < Parameters.crossover_rate:
            mother = self.selection(population)
            return Individual.construct_from_parents(father, mother)
        else:
            return Individual.construct_from_father(father)

    def survival(self, generation : List[Individual]) -> List[Individual]:
        # Survie déterministe : remplacement total de la population
        return generation

