def is_perfect_prime(n):
    """
    Checks whether a given number n is a perfect prime.
    
    A perfect prime is a prime number that is equal to the sum of its proper divisors (excluding itself).
    
    Args:
    n (int): The number to be checked.
    
    Returns:
    bool: True if the number is a perfect prime, False otherwise.
    """

    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Function to find the sum of proper divisors of a number
    def sum_of_divisors(num):
        sum_div = 1  # 1 is a divisor of all numbers
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                sum_div += i
                if i != num // i:  # Check if divisors are different
                    sum_div += num // i
        return sum_div

    # Check if the number is prime and equal to the sum of its proper divisors
    return is_prime(n) and n == sum_of_divisors(n)