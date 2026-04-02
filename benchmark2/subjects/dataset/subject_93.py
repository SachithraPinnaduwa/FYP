def count_valid_and_pairs(A):
    N = len(A)
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] & A[j] == A[i]:
                count += 1
    return count