def entance(side_length):
    if isinstance(side_length, (int, float)) and side_length > 0:
        area = (3**0.5 * side_length**2) / 4
        return round(area, 2)
    else:
        return "Invalid input value for side length"