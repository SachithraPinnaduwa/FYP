def find_max_adjacent_floors(budget):
    """
    Finds the plan with the maximal number of vertically adjacent floors whose total rental cost is exactly equal to the given budget.

    Parameters:
    budget (int): The total rental cost per month.

    Returns:
    tuple: A tuple containing two integers (start_floor, num_floors).
    """
    t = int((budget * 2) ** 0.5) + 1
    for i in range(t, 1, -1):
        if i % 2 == 1:
            if budget % i == 0 and budget // i > i // 2:
                return (budget // i - i // 2, i)
        elif budget % i != 0 and budget * 2 % i == 0 and (budget // i + 1 > i // 2):
            return (budget // i - i // 2 + 1, i)
    return (budget, 1)