def entrance(N):
    diagonal_sums = []
    for _ in range(N):
        matrix = [[(i * 110 + j) % 200 - 100 for j in range(4)] for i in range(4)]
        diagonal_sum = sum(matrix[i][i] for i in range(4))
        diagonal_sums.append(diagonal_sum)
    return diagonal_sums