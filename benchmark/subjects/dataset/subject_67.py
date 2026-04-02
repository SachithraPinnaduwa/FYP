import math

def compute_sum(x, K):
    total = sum(x)

    if total % K == 0:
        return format(total, ".2f")
    else:
        return math.ceil(total)