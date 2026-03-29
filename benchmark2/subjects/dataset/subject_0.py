import math

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    phi = (1 + math.sqrt(5)) / 2
    phi_n = phi ** n
    neg_phi_n = (-phi) ** (-n)
    
    return int((phi_n - neg_phi_n) / math.sqrt(5))