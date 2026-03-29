def sum_even(lst):
    return 0 if not lst else (lst[0] if lst[0] % 2 == 0 else 0) + sum_even(lst[1:])