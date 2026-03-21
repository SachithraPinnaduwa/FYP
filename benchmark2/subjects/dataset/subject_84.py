def fibonacci(n):
    if n <= 1:
        return n

    def multiply_matrices(a, b):
        x = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        y = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        z = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        w = a[1][0] * b[0][1] + a[1][1] * b[1][1]
        return [[x, y], [z, w]]

    def power(matrix, n):
        if n <= 1:
            return matrix

        half = power(matrix, n // 2)
        result = multiply_matrices(half, half)

        if n % 2 == 1:
            result = multiply_matrices(result, matrix)

        return result

    matrix = [[1, 1], [1, 0]]
    result = power(matrix, n - 1)
    return result[0][0]