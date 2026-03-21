def count_beautiful_fences(n: int, l: int, boards: list) -> int:
    MOD = 10 ** 9 + 7
    sze = 101
    
    dp = [[[0, 0] for _ in range(l + sze + 1)] for _ in range(n)]
    challengers = [[] for _ in range(sze)]
    
    for i in range(n):
        (a, b) = boards[i]
        if a != b:
            dp[i][a][1] = 1
            dp[i][b][0] = 1
        else:
            dp[i][a][1] = 1
        if a == b:
            challengers[a].append((a, i))
        else:
            challengers[a].append((b, i))
            challengers[b].append((a, i))
    
    for j in range(l + 1):
        for i in range(n):
            for z in range(2):
                if dp[i][j][z]:
                    for (a, ind) in challengers[boards[i][z]]:
                        if ind != i:
                            dp[ind][j + boards[i][z]][boards[ind].index(a)] = (dp[ind][j + boards[i][z]][boards[ind].index(a)] + dp[i][j][z]) % MOD
    
    cnt = 0
    for i in range(n):
        cnt = (cnt + dp[i][l][0] + dp[i][l][1]) % MOD
    
    return cnt