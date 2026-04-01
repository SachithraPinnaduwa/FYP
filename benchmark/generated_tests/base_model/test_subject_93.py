import unittest

class TestCountValidAndPairs(unittest.TestCase):

    def test_single_element_array(self):
        self.assertEqual(count_valid_and_pairs([10]), 0)

    def test_all_elements_equal(self):
        self.assertEqual(count_valid_and_pairs([1, 1, 1, 1, 1]), 10)

    def test_no_common_bitwise_and(self):
        self.assertEqual(count_valid_and_pairs([10, 20, 30, 40]), 0)

    def test_mixed_elements(self):
        self.assertEqual(count_valid_and_pairs([1, 2, 3, 4, 5]), 6)

    def test_large_number_of_pairs(self):
        arr = list(range(1, 101))
        self.assertEqual(count_valid_and_pairs(arr), 9850)

if __name__ == '__main__':
    unittest.main()