def sum_list_recursive(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_list_recursive(lst[1:])