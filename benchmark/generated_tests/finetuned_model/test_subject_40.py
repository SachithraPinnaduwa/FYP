def test_min_increment_operations():
    assert min_increment_operations([1, 2, 2], 3) == 1
    assert min_increment_operations([1, 1, 2, 3], 4) == 3
    assert min_increment_operations([4, 4, 4, 4], 4) == 6
    assert min_increment_operations([1, 2, 3, 4], 4) == 0
    assert min_increment_operations([1000000000, 1000000000, 1000000000], 3) == 2999999998
    assert min_increment_operations([1, 2, 3, 1000000000, 1000000001], 5) == 2
    assert min_increment_operations([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10) == 45
    assert min_increment_operations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 0
    assert min_increment_operations([1, 2, 3, 4, 5, 6, 7, 8, 9, 1000000000], 10) == 4500000000
    assert min_increment_operations([1000000000, 1000000000, 1000000000, 1000000000, 1000000000], 5) == 12499999975
    assert min_increment_operations([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 55
    assert min_increment_operations([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 12) == 91
    assert min_increment_operations([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 13) == 136