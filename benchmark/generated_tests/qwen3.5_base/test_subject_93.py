import unittest

class TestCountValidAndPairs(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_valid_and_pairs([]), 0)

    def test_single_element(self):
        self.assertEqual(count_valid_and_pairs([1]), 0)

    def test_two_elements(self):
        self.assertEqual(count_valid_and_pairs([1, 2]), 1)

    def test_three_elements(self):
        self.assertEqual(count_valid_and_pairs([1, 2, 3]), 2)

    def test_all_elements(self):
        self.assertEqual(count_valid_and_pairs([1, 2, 3, 4]), 6)

    def test_large_list(self):
        self.assertEqual(count_valid_and_pairs(list(range(100))), 4950)

if __name__ == '__main__':
    unittest.main()
