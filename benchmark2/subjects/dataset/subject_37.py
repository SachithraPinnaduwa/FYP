def isOddPrimeGreaterThan100(number):
    if number <= 100 or number % 2 == 0:  # Check if number is less than or equal to 100 or even
        return False
    for i in range(3, int(number**0.5) + 1, 2):  # Check divisibility by odd numbers only
        if number % i == 0:
            return False
    return True

def findSecondSmallestOddPrimeGreaterThan100(array):
    smallest = secondSmallest = float('inf')
    for number in array:
        if isOddPrimeGreaterThan100(number):
            if number < smallest:
                secondSmallest = smallest
                smallest = number
            elif number < secondSmallest and number != smallest:
                secondSmallest = number
    return secondSmallest