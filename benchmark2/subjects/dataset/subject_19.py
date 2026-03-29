def minimum_difference_of_sums(n: int) -> int:
    """
    Calculate the minimum possible value of the absolute difference between the sums of two sets A and B
    when dividing the sequence 1, 2, ..., n into two sets.

    Parameters:
    n (int): The integer representing the length of the sequence from 1 to n.

    Returns:
    int: The minimum possible value of the absolute difference between the sums of two sets A and B.
    """
    return (n * (n + 1) // 2) % 2