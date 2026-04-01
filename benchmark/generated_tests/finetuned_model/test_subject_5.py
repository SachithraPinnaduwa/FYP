import unittest

class TestFindLexicographicallyPrecedingPermutation(unittest.TestCase):
    
    # Test case for the sample input
    def test_sample_input(self):
        n = 3
        permutation = [1, 3, 2]
        expected_output = [1, 2, 3]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)
    
    # Test case for the input permutation being already the lexicographically least permutation
    def test_already_lexicographically_least(self):
        n = 3
        permutation = [1, 2, 3]
        expected_output = [1, 2, 3]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)
    
    # Test case for an input permutation with more than two elements
    def test_multiple_elements(self):
        n = 5
        permutation = [5, 3, 4, 2, 1]
        expected_output = [5, 2, 4, 1, 3]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)
    
    # Test case for an input permutation with only two elements
    def test_two_elements(self):
        n = 2
        permutation = [2, 1]
        expected_output = [1, 2]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)
    
    # Test case for an input permutation with a single element
    def test_single_element(self):
        n = 1
        permutation = [1]
        expected_output = [1]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)
    
    # Test case for an input permutation with duplicate elements
    def test_duplicate_elements(self):
        n = 3
        permutation = [1, 1, 1]
        expected_output = [1, 1, 1]
        self.assertEqual(find_lexicographically_preceding_permutation(n, permutation), expected_output)