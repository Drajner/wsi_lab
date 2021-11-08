from cec2017.functions import f4
import numpy as np
import random

UPPER_BOUND = 100
ELITE_SIZE = 3
MUTATION_POWER = 0.1
POPULATION_SIZE = 60

def find_best(rating, population):
    best_rate = min(rating)
    return population[rating.index(best_rate)], best_rate


def tournament_reproduction(population, rating, population_size):
    new_population = []
    for i in range(population_size):
        opponent1 = random.randint(0, len(population)-1)
        opponent2 = random.randint(0, len(population)-1)
        if rating[opponent1] >= rating[opponent2]:
            new_population.append(population[opponent2])
        else:
            new_population.append(population[opponent1])
    return new_population


def mutation(population, mutation_power):
    mutated_population = []
    for specimen in population:
        mutated_specimen = [(value + mutation_power * random.gauss(0, 1)) for value in specimen]
        mutated_population.append(mutated_specimen)
    return mutated_population


def elite_succesion(population, mutated_population, rating, mutated_rating, elite_size):
    population_rated = []
    for i in range(len(population)):
        population_rated.append([rating[i],population[i]])

    population_rated.sort(reverse=True)
    population_rated = population_rated[:elite_size]

    mut_population_rated = []
    for i in range(len(population)):
        mut_population_rated.append([mutated_rating[i],mutated_population[i]])

    mut_population_rated.sort()
    mut_population_rated = mut_population_rated[elite_size:]

    new_population = []
    for rated_specimen in population_rated:
        new_population.append(rated_specimen[1])
    for rated_specimen in mut_population_rated:
        new_population.append(rated_specimen[1])

    return new_population


def evo_algorythm(fun, starting_population, population_size, mutation_power, max_generations, elite_size):
    generation = 0
    rating = [fun(specimen) for specimen in starting_population]
    population = starting_population
    best_specimen, best_rating = find_best(rating, population)
    while generation < max_generations:
        reproduced_population = tournament_reproduction(population, rating, population_size)
        mutated_population = mutation(reproduced_population, mutation_power)
        mutated_rating = [fun(specimen) for specimen in mutated_population]
        mut_best_specimen, mut_best_rating = find_best(mutated_rating, mutated_population)
        if mut_best_rating <= best_rating:
            best_rating = mut_best_rating
            best_specimen = mut_best_specimen
        population = elite_succesion(population, mutated_population, rating, mutated_rating, elite_size)
        generation += 1
    return [best_specimen, best_rating]


def main():
    results = []
    for j in range(25):
        population = []
        for i in range(POPULATION_SIZE):
            population.append(np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=2))
        results.append(evo_algorythm(f4, population, POPULATION_SIZE, MUTATION_POWER, 10000, ELITE_SIZE)[1])
        print(str(j+1) + " run of the algorythm is finished")
    print("*****")
    string = "Population size: " + str(POPULATION_SIZE)
    string += "   Mutation power: " + str(MUTATION_POWER)
    string += "   Elite size: " + str(ELITE_SIZE)
    string += "   min: " + str(min(results))
    string += "   avg: " + str(np.average(results))
    string += "   std: " + str(np.std(results, ddof=1))
    string += "   max: " + str(max(results))
    print(string)
    #print("Population size: " + str(POPULATION_SIZE) +  "   Mutation power: " + str(MUTATION_POWER) + "   Elite size: " + str(ELITE_SIZE))
    #print("min: " + str(min(results)))
    #print("   avg: " + str(np.average(results)))
    #print("   std: " + str(np.std(results, ddof=1)))
    #print("   max: " + str(max(results)))
    print("*****")


if __name__ == "__main__":
    main()
