def entance(n):
    if n <= 1:
       return n
    else:
       return (entance(n-1) + entance(n-2))