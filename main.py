from labs.lab03 import determinant

print("--- Matrix Determinant (recursive) ---")
n = int(input("--- Enter the size of the matrix (n for n x n): "))
matrix = []
print("--- Enter the rows of the matrix (separate numbers with spaces):")
for i in range(n):
    row = list(map(float, input(f"--Row {i + 1}: ").split()))
    if len(row) != n:
        raise ValueError("--Each row must have exactly n elements.")
    matrix.append(row)
result = determinant(matrix)
print("--- Result:", result)