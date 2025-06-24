import random

def monte_carlo_integration(func, a, b, num_samples):
    if a >= b:
        raise ValueError("-- Lower bound 'a' must be less than upper bound 'b'.")
    if num_samples <= 0:
        raise ValueError("-- Number of samples must be positive.")

    total = 0.0
    for _ in range(num_samples):
        x = random.uniform(a, b)
        total += func(x)

    return (b - a) * total / num_samples
