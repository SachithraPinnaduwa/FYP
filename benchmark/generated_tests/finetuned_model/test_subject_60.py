def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 4
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 9
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 0
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11) == -1
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1) == -1
    assert binary_search([], 5) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 10) == -1
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([10, 20, 30, 40, 50, 60, 70, 80, 90], 40) == 3
    assert binary_search([10, 20, 30, 40, 50, 60, 70, 80, 90], 5) == -1