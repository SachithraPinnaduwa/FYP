def find_median(data):
    """
    This function takes a list of numbers as input, sorts the list in ascending order, 
    and returns the median value. It handles both even and odd-length lists.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The median value of the input list.
    """
    # organizing the list in ascending sequence
    data.sort()
    # Finding the middle figure from the sorted sequence
    n = len(data)
    if n % 2 == 0:
        median = (data[n//2 - 1] + data[n//2]) / 2
    else:
        median = data[n//2]
    return median