def max_tower_height(n, rings):
    aux = [(float('inf'), 0, 0)]  # Initialize with a sentinel value
    for a, b, h in rings:
        aux.append((b, a, h))
    aux.sort(reverse=True)
    
    s = [0]
    p = [0] * (n + 1)
    
    for i in range(1, n + 1):
        while aux[s[-1]][1] >= aux[i][0]:
            s.pop()
        p[i] = p[s[-1]] + aux[i][2]
        s.append(i)
    
    return max(p)