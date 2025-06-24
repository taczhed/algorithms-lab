from labs.lab06 import genetic_algorithm
import math

print("--- Genetic Algorithm Optimization ---")
print("--- Enter function to maximize (e.g. 'math.sin(x)', '-(x-2)**2 + 3')")

expr = input("-- Function f(x): ")
a = float(input("-- Search start (a): "))
b = float(input("-- Search end (b): "))
pop_size = int(input("-- Population size: "))
gens = int(input("-- Number of generations: "))
mut_rate = float(input("-- Mutation rate (e.g. 0.1): "))
tournament = int(input("-- Tournament size: "))

# Define the function from user input
def f(x):
    return eval(expr, {"x": x, "math": math})

result = genetic_algorithm(f, (a, b), pop_size, gens, mut_rate, tournament)
print("--- Best solution found (x):", result)
print("--- f(x) =", f(result))
