class Parameters(object):
    # Paramètres concernant la population et l'algorithme
    individuals_nb : int = 20               # Nombre d'individus par génération
    generations_max_nb : int = 50           # Nombre maximal de générations
    initial_genes_nb : int = 10             # Nombre initial de gènes si le génome est de taille variable
    min_fitness : int = 0                   # Valeur d'adaptation à atteindre (Fitness)
    # Taux utilisés lors de la reproduction
    mutations_rate : float = 0.10           # Taux de mutations
    mutations_add_rate : float = 0.20       # Taux d'ajout de gènes
    mutation_delete_rate : float = 0.10     # Taux de suppression de gènes
    crossover_rate : float = 0.60           # Taux de croisements (Crossover)
