def sieve_of_eratosthenes(n):
    if n < 2:
        return []

    # Create a list initialized with 1 (assuming all numbers are prime)
    sieve = [0, 0]
    for i in range(n - 1):
        sieve.append(1)

    # Iterate from 2 up to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 1:
            # Mark all multiples of i as non-prime (0)
            for j in range(i * i, n + 1, i):
                sieve[j] = 0

    # Return a list of prime numbers
    primes = []
    for i in range(n + 1):
        if sieve[i] == 1:
            primes.append(i)

    return primes