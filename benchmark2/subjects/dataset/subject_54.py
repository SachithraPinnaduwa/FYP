def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_three_odd_primes(array):
    odd_primes = [num for num in array if num % 2 != 0 and is_prime(num)]
    return len(odd_primes) >= 3 and is_prime(sum(odd_primes))