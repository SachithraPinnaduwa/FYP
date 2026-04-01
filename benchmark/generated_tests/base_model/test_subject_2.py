import unittest

class TestBottomUpCutRod(unittest.TestCase):

    def test_base_case(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 1
        expected_revenue = 1
        expected_lengths = [1]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_lengths))

    def test_single_piece(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 4
        expected_revenue = 8
        expected_lengths = [4]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_lengths))

    def test_multiple_pieces(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 7
        expected_revenue = 17
        expected_lengths = [7]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_lengths))

    def test_optimal_solution(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 10
        expected_revenue = 30
        expected_lengths = [10]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_lengths))

    def test_no_profit(self):
        p = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        n = 5
        expected_revenue = 0
        expected_lengths = []
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_lengths))

    def test_large_input(self):
        p = [0] + list(range(1, 1001))
        n = 1000
        expected_revenue = 500500
        expected_lengths = [1000]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_lengths))

if __name__ == '__main__':
    unittest.main()