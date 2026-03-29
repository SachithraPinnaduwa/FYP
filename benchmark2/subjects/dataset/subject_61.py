def count_king_moves(R, C, K):
    # Calculate the range of rows and columns the king can move to
    a = min(8, R + K) - max(1, R - K) + 1
    b = min(8, C + K) - max(1, C - K) + 1
    
    # Return the total number of squares the king can visit
    return a * b