import random

def genetic_algorithm(func, bounds, population_size, generations, mutation_rate, tournament_size):
    min_x, max_x = bounds

    def random_individual():
        return random.uniform(min_x, max_x)

    def mutate(x):
        # Gaussian mutation within bounds
        delta = (max_x - min_x) * 0.1
        x_new = x + random.gauss(0, delta)
        return min(max(x_new, min_x), max_x)

    def crossover(x1, x2):
        alpha = random.random()
        return alpha * x1 + (1 - alpha) * x2

    def select(population):
        # Tournament selection
        candidates = random.sample(population, tournament_size)
        return max(candidates, key=func)

    # Initialize population
    population = [random_individual() for _ in range(population_size)]

    for _ in range(generations):
        new_population = []
        for _ in range(population_size):
            parent1 = select(population)
            parent2 = select(population)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child = mutate(child)
            new_population.append(child)
        population = new_population

    return max(population, key=func)
