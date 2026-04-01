import unittest

class TestBottomUpCutRod(unittest.TestCase):
    # Test case for a simple rod of length 2 with prices [0, 0, 5, 8]
    def test_simple_rod(self):
        p = [0, 0, 5, 8]
        n = 2
        expected_revenue = 8
        expected_cut_sizes = [2]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

    # Test case for a rod of length 4 with prices [0, 0, 5, 8, 9]
    def test_rod_of_length_4(self):
        p = [0, 0, 5, 8, 9]
        n = 4
        expected_revenue = 10
        expected_cut_sizes = [2, 2]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

    # Test case for a rod of length 10 with prices [0, 0, 1, 5, 8, 9, 10, 17, 17, 20, 24]
    def test_rod_of_length_10(self):
        p = [0, 0, 1, 5, 8, 9, 10, 17, 17, 20, 24]
        n = 10
        expected_revenue = 30
        expected_cut_sizes = [10]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

    # Test case for a rod of length 1 with price 0
    def test_rod_of_length_1(self):
        p = [0, 0]
        n = 1
        expected_revenue = 0
        expected_cut_sizes = [1]
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))

    # Test case for a rod of length 0 with price 0
    def test_rod_of_length_0(self):
        p = [0]
        n = 0
        expected_revenue = 0
        expected_cut_sizes = []
        self.assertEqual(bottom_up_cut_rod(p, n), (expected_revenue, expected_cut_sizes))