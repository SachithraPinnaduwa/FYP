import unittest

class TestBottomUpCutRod(unittest.TestCase):
    def test_basic_cases(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 4
        expected_revenue = 10
        expected_cut_sizes = [1, 3]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

    def test_single_piece_case(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 1
        expected_revenue = 1
        expected_cut_sizes = [1]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

    def test_zero_length_case(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 0
        expected_revenue = 0
        expected_cut_sizes = []
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

    def test_single_item_case(self):
        p = [0, 1]
        n = 1
        expected_revenue = 1
        expected_cut_sizes = [1]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

    def test_multiple_pieces_case(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 9
        expected_revenue = 25
        expected_cut_sizes = [1, 2, 6]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

    def test_max_price_case(self):
        p = [0, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
        n = 10
        expected_revenue = 10000
        expected_cut_sizes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

    def test_mixed_case(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 8
        expected_revenue = 22
        expected_cut_sizes = [2, 6]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

if __name__ == '__main__':
    unittest.main()