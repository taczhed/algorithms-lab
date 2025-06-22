def determinant(matrix):
    # Removes the i-th row and j-th column from the matrix
    def minor(mat, i, j):
        return [row[:j] + row[j+1:] for idx, row in enumerate(mat) if idx != i]

    # Recursive function to compute the determinant
    def det(mat):
        n = len(mat)

        # Base case: 1x1 matrix, the determinant is the single value
        if n == 1:
            return mat[0][0]

        # Base case: 2x2 matrix, use the direct formula
        if n == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

        # Recursive case: Expand along the first row (Laplace expansion)
        return sum(
            (-1) ** col * mat[0][col] * det(minor(mat, 0, col))
            for col in range(n)
        )

    return det(matrix)