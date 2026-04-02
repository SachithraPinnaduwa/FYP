def nth_prime(N):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    num = 2
    while(count < N):
        if is_prime(num):
            count += 1
        num += 1
    return num - 1