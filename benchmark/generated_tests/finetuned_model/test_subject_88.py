import unittest

class TestMinDeviationShift(unittest.TestCase):

    def test_identical_permutation(self):
        # Test case for an identical permutation (id 0)
        n = 3
        p = [1, 2, 3]
        expected_res = 0
        expected_ires = 0
        self.assertEqual(find_min_deviation_shift(n, p), (expected_res, expected_ires))

    def test_cyclic_shift_with_min_deviation(self):
        # Test case for a permutation with cyclic shift having minimum deviation
        n = 3
        p = [2, 3, 1]
        expected_res = 0
        expected_ires = 1
        self.assertEqual(find_min_deviation_shift(n, p), (expected_res, expected_ires))

    def test_cyclic_shift_with_max_deviation(self):
        # Test case for a permutation with cyclic shift having maximum deviation
        n = 3
        p = [3, 2, 1]
        expected_res = 2
        expected_ires = 1
        self.assertEqual(find_min_deviation_shift(n, p), (expected_res, expected_ires))

    def test_large_permutation(self):
        # Test case for a larger permutation
        n = 1000000
        p = list(range(1, n + 1))
        p[0], p[1] = p[1], p[0]
        expected_res = 0
        expected_ires = 0
        self.assertEqual(find_min_deviation_shift(n, p), (expected_res, expected_ires))

    def test_permutation_with_negative_values(self):
        # Test case for a permutation with negative values (should not occur as per problem statement)
        n = 3
        p = [3, -1, 2]
        with self.assertRaises(AssertionError):
            find_min_deviation_shift(n, p)