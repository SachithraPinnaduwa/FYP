def find_lexicographically_preceding_permutation(n, permutation):
    b = []
    flag = 0
    
    for x in range(n-1, 0, -1):
        b = permutation[:x-1]
        if permutation[x] < permutation[x-1]:
            for y in range(n-1, x-1, -1):
                if permutation[x-1] > permutation[y]:
                    b.append(permutation[y])
                    flag = 1
                    c = permutation[x-1:]
                    del(c[y-x+1])
                    c.sort()
                    c.reverse()
                    b = b + c
                if flag == 1:
                    break
        if flag == 1:
            break
    
    if flag == 0:
        return permutation
    else:
        return b