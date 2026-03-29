import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def validate_input():
    while True:
        try:
            num = int(input("Enter a number between 2 and 10 (inclusive), divisible by 5, and not prime: "))
            if num >= 2 and num <= 10 and num % 5 == 0 and not is_prime(num):
                return num
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")