def test_count_beautiful_fences():
    assert count_beautiful_fences(2, 3, [(1, 2), (2, 3)]) == 2
    assert count_beautiful_fences(1, 2, [(2, 2)]) == 1
    assert count_beautiful_fences(6, 6, [(2, 1), (3, 2), (2, 5), (3, 3), (5, 1), (2, 1)]) == 20
    assert count_beautiful_fences(3, 5, [(1, 2), (2, 3), (3, 1)]) == 12
    assert count_beautiful_fences(4, 4, [(2, 2), (3, 3), (4, 4), (5, 5)]) == 4
    assert count_beautiful_fences(2, 6, [(1, 2), (3, 3)]) == 0
    assert count_beautiful_fences(1, 1, [(1, 1)]) == 1
    assert count_beautiful_fences(5, 10, [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]) == 0
    assert count_beautiful_fences(3, 10, [(1, 2), (2, 3), (3, 1)]) == 72
    assert count_beautiful_fences(4, 12, [(2, 2), (3, 3), (4, 4), (5, 5)]) == 60