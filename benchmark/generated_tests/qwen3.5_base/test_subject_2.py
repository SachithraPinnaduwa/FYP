import unittest

class TestBottomUpCutRod(unittest.TestCase):
    def test_bottom_up_cut_rod(self):
        # Test case 1
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 7
        expected_revenue = 22
        expected_cut_sizes = [1, 6]
        result = bottom_up_cut_rod(p, n)
        self.assertEqual(result[0], expected_revenue)
        self.assertEqual(result[1], expected_cut_sizes)

        # Test case 2
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 8
        expected_revenue = 25
        expected_cut_sizes = [1, 7]
        result = bottom_up_cut_rod(p, n)
        self.assertEqual(result[0], expected_revenue)
        self.assertEqual(result[1], expected_cut_sizes)

        # Test case 3
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 9
        expected_revenue = 28
        expected_cut_sizes = [1, 8]
        result = bottom_up_cut_rod(p, n)
        self.assertEqual(result[0], expected_revenue)
        self.assertEqual(result[1], expected_cut_sizes)

        # Test case 4
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 10
        expected_revenue = 30
        expected_cut_sizes = [1, 9]
        result = bottom_up_cut_rod(p, n)
        self.assertEqual(result[0], expected_revenue)
        self.assertEqual(result[1], expected_cut_sizes)

        # Test case 5
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 11
        expected_revenue = 33
        expected_cut_sizes = [1, 10]
        result = bottom_up_cut_rod(p, n)
        self.assertEqual(result[0], expected_revenue)
        self.assertEqual(result[1], expected_cut_sizes)

        # Test case 6
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 12
        expected_revenue = 35
        expected_cut_sizes = [1, 11]
        result = bottom_up_cut_rod(p, n)
        self.assertEqual(result[0], expected_revenue)
        self.assertEqual(result[1], expected_cut_sizes)

        # Test case 7
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 13
        expected_revenue = 38
        expected_cut_sizes = [1, 12]
        result = bottom_up_cut_rod(p, n)
        self.assertEqual(result[0], expected_revenue)
        self.assertEqual(result[1], expected_cut_sizes)

        # Test case 8
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 14
        expected_revenue = 40
        expected_cut_sizes = [1, 13]
        result = bottom_up_cut_rod(p, n)
        self.assertEqual(result[0], expected_revenue)
        self.assertEqual(result[1], expected_cut_sizes)

        # Test case 9
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 15
        expected_revenue = 43
        expected_cut_sizes = [1, 14]
        result = bottom_up_cut_rod(p, n)
        self.assertEqual(result[0], expected_revenue)
        self.assertEqual(result[1], expected_cut_sizes)

        # Test case 10
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 16
        expected_revenue = 45
        expected_cut_sizes = [1, 15]
        result = bottom_up_cut_rod(p, n)
        self.assertEqual(result[0], expected_revenue)
        self.assertEqual(result[1], expected_cut_sizes)

        # Test case 11
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 17
        expected_revenue = 48
        expected_cut_sizes = [1, 16]
        result = bottom_up_cut_rod(p, n)
        self.assertEqual(result[0], expected_revenue)
        self.assertEqual(result[1], expected_cut_sizes)

        # Test case 12
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 18
        expected_revenue = 50
        expected_cut_sizes = [1, 17]
        result = bottom_up_cut_rod(p, n)
        self.assertEqual(result[0], expected_revenue)
        self.assertEqual(result[1], expected_cut_sizes)

        # Test case 13
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 19
        expected_revenue = 53
        expected_cut_sizes = [1, 18]
        result = bottom_up_cut_rod(p, n)
        self.assertEqual(result[0], expected_revenue)
        self.assertEqual(result[1], expected_cut_sizes)

        # Test case 14
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 20
        expected_revenue = 55
        expected_cut_sizes = [1, 19]
        result = bottom_up_cut_rod(p, n)
        self.assertEqual(result[0], expected_revenue)
        self.assertEqual(result[1], expected_cut_sizes)

        # Test case 15
        p = [0, 1, 5, 8, 9, 10, 17, 17]
        n = 21
        expected_revenue = 58
        expected_cut_sizes = [