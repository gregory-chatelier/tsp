from tsp_genetic_algorithm import Parameters, EvolutionaryProcess

Parameters.crossover_rate = 0.6
Parameters.mutations_rate = 0.1
Parameters.mutations_add_rate = 0.2
Parameters.mutation_delete_rate = 0.1
Parameters.min_fitness = 0
Parameters.generations_max_nb = 200

ga = EvolutionaryProcess()
ga.run()