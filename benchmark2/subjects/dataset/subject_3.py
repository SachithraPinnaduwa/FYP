def factorial_(num):
    """Find the factorial of a given number"""
    # base case: factorial of 0 & 1 is 1
    if num == 0 or num == 1:
        return 1
    else:
        # recursive case: n! = n * (n-1)!
        return num * factorial_(num - 1)