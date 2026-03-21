def find_k_for_digit_power_sum(n, p):
    s = 0
    for i, c in enumerate(str(n)):
        s += pow(int(c), p + i)
    return s // n if s % n == 0 else -1