def sum_of_primes(n):
    """
    Calculate the sum of all prime numbers between 1 and n (inclusive) using a list comprehension.

    Args:
        n (int): The upper limit for the range of prime numbers.

    Returns:
        int: The sum of prime numbers between 1 and n.
    """
    return sum([num for num in range(2, n + 1) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))])