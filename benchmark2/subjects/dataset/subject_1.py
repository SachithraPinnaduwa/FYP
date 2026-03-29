def median_in_interval(numbers, lower_limit, upper_limit):
    numbers.sort()
    if len(numbers) % 2 == 0:  # Even number of elements
        median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
    else:  # Odd number of elements
        median = numbers[len(numbers)//2]
    return lower_limit <= median <= upper_limit