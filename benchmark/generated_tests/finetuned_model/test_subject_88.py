import unittest

class TestFindMinDeviationShift(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(find_min_deviation_shift(3, [1, 2, 3]), (0, 0))

    def test_example_2(self):
        self.assertEqual(find_min_deviation_shift(3, [2, 3, 1]), (0, 1))

    def test_example_3(self):
        self.assertEqual(find_min_deviation_shift(3, [3, 2, 1]), (2, 1))

    def test_single_element_permutation(self):
        self.assertEqual(find_min_deviation_shift(1, [1]), (0, 0))

    def test_small_random_permutation(self):
        self.assertEqual(find_min_deviation_shift(5, [2, 1, 4, 3, 5]), (2, 3))

    def test_large_random_permutation(self):
        import random
        n = 1000
        p = list(range(1, n + 1))
        random.shuffle(p)
        res, ires = find_min_deviation_shift(n, p)
        expected_res = sum(abs(p[i] - (i + 1)) for i in range(n))
        expected_ires = 0  # The identity permutation has the minimum deviation
        self.assertEqual((res, ires), (expected_res, expected_ires))

if __name__ == '__main__':
    unittest.main()