# Algorithmes génétiques : voyageur de commerce

Ce projet est un port sous Python de l'implémentation C# d'un algorithme génétique qui accompagne le livre [*L'Intelligence Artificielle pour les développeurs Concepts et implémentations en C#*](https://www.editions-eni.fr/livre/l-intelligence-artificielle-pour-les-developpeurs-concepts-et-implementations-en-c-2e-edition-9782409011405), par Virginie MATHIVET, ouvrage paru aux éditions ENI.

Tous les concepts sont détaillés dans le livre, le code Python ne sera pas documenté. Je vous recommande l'achat du livre qui couvre de façon pragmatique un ensemble de techniques d'IA.

Cette version Python est une migration du code C# propre au problème du voyageur de commerce (ou encore TSP en anglais, Travelling Salesman Problem)



## Pourquoi cette migration ? 

J'ai eu besoin de vérifier par un prototype la validité d'un algorithme génétique pour la résolution d'un problème métier non déterministe. Le langage Python est bien adapté à la réalisation de tels prototypes rapides et la transcription du problème du voyageur de commerce m'a servi de fondation au prototype. Le code projet est très simple mais peut vous faire gagner du temps sur un besoin similaire.



## Par où commencer

Le [problème du voyageur de commerce](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce) est très bien documenté sur Wikipédia (par ex.), je ne reviendrai pas sur sa définition.

Le programme va chercher à minimiser le nombre de kilomètres à parcourir pour un trajet entre 7 villes : Paris, Lyon, Marseille, Nantes, Bordeaux, Toulouse, Lille. La distance entre chaque ville est connue et elle est exprimée dans un tableau, le distancier, qui est renseigné dans la classe qui décrit le problème : *tsp_genetic_algorithm/problem.py*



```python
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
        ...
```



Exécutez le script point d'entrée du programme :

```bash
python tsp.py
```

Le déroulement affiche la meilleure solution à chaque génération sur un nombre prédéterminé de générations.

```bash
Génération 0 -> 3244 :Nantes - Bordeaux - Toulouse - Marseille - Paris - Lille - Lyon
Génération 1 -> 2991 :Nantes - Bordeaux - Toulouse - Lyon - Marseille - Paris - Lille
Génération 2 -> 2991 :Nantes - Bordeaux - Toulouse - Lyon - Marseille - Paris - Lille
Génération 3 -> 2991 :Nantes - Bordeaux - Toulouse - Lyon - Marseille - Paris - Lille
Génération 4 -> 2579 :Nantes - Bordeaux - Toulouse - Marseille - Lyon - Lille - Paris
Génération 5 -> 2579 :Nantes - Bordeaux - Toulouse - Marseille - Lyon - Lille - Paris
...
Génération 199 -> 2579 :Nantes - Bordeaux - Toulouse - Marseille - Lyon - Lille - Paris
```

L'optimum de 2579 Km est trouvé dans l'exemple à la 5ème génération.