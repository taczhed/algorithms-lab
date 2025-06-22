from labs.lab04 import root_bisection

print("--- Root of 5th-Degree Polynomial ---")
print("--- Enter polynomial coefficients from x^0 to x^5 (space separated):")
coeffs = list(map(float, input("-- Coefficients: ").split()))
if len(coeffs) != 6:
    raise ValueError("-- Polynomial must have exactly 6 coefficients (degree 5).")

a = float(input("-- Interval start (a): "))
b = float(input("-- Interval end (b): "))
eps = float(input("-- Precision (e.g. 0.0001): "))

result = root_bisection(coeffs, a, b, eps)
print("--- Root found:", result)