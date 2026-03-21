def calculate_robot_locations(n: int) -> int:
    if n % 2 == 0:
        return int((n - n / 2 + 1) ** 2)
    else:
        return int((n + 2) * ((n + 2) // 2) + (n + 2) // 2)