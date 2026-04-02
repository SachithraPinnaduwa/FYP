def test_minimum_cost_arborescence():
    assert minimum_cost_arborescence(4, 6, 0, [(0, 1, 3), (0, 2, 2), (2, 0, 1), (2, 3, 1), (3, 0, 1), (3, 1, 5)]) == 6
    assert minimum_cost_arborescence(6, 10, 0, [(0, 2, 7), (0, 1, 1), (0, 3, 5), (1, 4, 9), (2, 1, 6), (1, 3, 2), (3, 4, 3), (4, 2, 2), (2, 5, 8), (3, 5, 3)]) == 11
    assert minimum_cost_arborescence(5, 7, 0, [(0, 1, 10), (0, 2, 5), (1, 2, 3), (1, 3, 1), (2, 4, 7), (3, 4, 4), (3, 0, 8)]) == 17
    assert minimum_cost_arborescence(3, 3, 0, [(0, 1, 5), (0, 2, 3), (2, 1, 2)]) == 6
    assert minimum_cost_arborescence(2, 1, 0, [(0, 1, 10)]) == 10
    assert minimum_cost_arborescence(5, 4, 0, [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 0, 4)]) == 10
    assert minimum_cost_arborescence(4, 5, 0, [(0, 1, 5), (1, 2, 1), (2, 3, 1), (3, 0, 2), (1, 3, 3)]) == 8
    assert minimum_cost_arborescence(3, 3, 0, [(0, 1, 10), (1, 2, 10), (2, 0, 10)]) == 30
    assert minimum_cost_arborescence(4, 4, 0, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1)]) == 4
    assert minimum_cost_arborescence(5, 6, 0, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 0, 1), (0, 2, 1)]) == 5