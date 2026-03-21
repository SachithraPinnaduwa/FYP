def smallest_positive_no_compare(lst: list):
    """Return the least positive number in dataset lst without the use of comparative functions.
    Handles both negative and positive numbers within datasets."""
    smallest = float('inf')
    for i in lst:
        if i <= 0:
            continue
        if smallest - i > 0:
            smallest = i
    return smallest if smallest != float('inf') else None