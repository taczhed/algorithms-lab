def lcm(a, b):
    while b != 0:
        t = a % b
        a = b
        b = t
    return a