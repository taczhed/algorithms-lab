from labs.lab05 import monte_carlo_integration
import math

print("--- Monte Carlo Integration ---")
print("--- Enter function to integrate (e.g. 'math.sin(x)', 'x**2 + 1')")

expr = input("-- Function f(x): ")
a = float(input("-- Interval start (a): "))
b = float(input("-- Interval end (b): "))
n = int(input("-- Number of samples: "))

# Define the function from user input
def f(x):
    return eval(expr, {"x": x, "math": math})

result = monte_carlo_integration(f, a, b, n)
print("--- Approximated integral:", result)

# abs(math.sin(x)+math.sin(2*x)+math.sin(4*x)+math.sin(8*x))
# 0
# 6.283185
# 1000000