def minimum_moves(start_x, start_y, end_x, end_y):
    if start_x == end_x or start_y == end_y:
        return 2
    else:
        return 1