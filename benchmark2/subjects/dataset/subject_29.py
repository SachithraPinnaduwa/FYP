def detect_even_odd(number):
    if not isinstance(number, int) or number <= 0 or number > 1000:
        return "Invalid Input"
    elif number % 2 == 0:
        return "Even"
    else:
        return "Odd"