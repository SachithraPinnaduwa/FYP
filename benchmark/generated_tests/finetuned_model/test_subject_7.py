from typing import List, Tuple

def test_count_and_indices():
    assert count_and_indices([1, 2, 4, 4, 4, 5, 6], 4) == (3, [2, 3, 4])
    assert count_and_indices([1, 1, 1, 1, 1, 1, 1], 1) == (7, [0, 1, 2, 3, 4, 5, 6])
    assert count_and_indices([2, 3, 5, 7, 11, 13, 17], 5) == (1, [2])
    assert count_and_indices([10, 20, 30, 40, 50], 25) == (0, [])
    assert count_and_indices([100, 100, 100], 100) == (3, [0, 1, 2])
    assert count_and_indices([1, 3, 5, 7, 9, 9, 9, 11, 13], 9) == (3, [4, 5, 6])
    assert count_and_indices([1, 1, 2, 2, 3, 3, 3, 3], 3) == (4, [4, 5, 6, 7])
    assert count_and_indices([1000000000, 1000000000, 1000000000], 1000000000) == (3, [0, 1, 2])
    assert count_and_indices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11) == (0, [])
    assert count_and_indices([1], 1) == (1, [0])