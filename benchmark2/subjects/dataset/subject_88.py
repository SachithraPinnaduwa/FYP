def find_min_deviation_shift(n, p):
    res = 0
    ires = 0
    neg = 0
    when = [0] * n
    
    # Transform the permutation to calculate initial deviation
    for i in range(n):
        p[i] = i + 1 - p[i]
        res += abs(p[i])
        if p[i] <= 0:
            neg += 1
        a = -p[i]
        if a < 0:
            a = a + n
        when[a] += 1
    
    ares = res
    
    # Calculate the deviation for each cyclic shift
    for i in range(n):
        neg -= when[i]
        ares -= neg
        ares += n - neg
        x = p[n - i - 1] + i + 1
        ares -= x
        ares += n - x
        neg += 1
        if ares < res:
            res = ares
            ires = i + 1
    
    return res, ires