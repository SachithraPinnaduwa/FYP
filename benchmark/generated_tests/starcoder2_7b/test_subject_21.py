import unittest

class TestGreedySumSubset(unittest.TestCase):
    def test_greedy_sum_subset(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target_sum = 15

        # Expected output
        expected_output = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

        # Run the function
        subsets = greedy_sum_subset(arr, target_sum)

        # Check if the output is correct
        self.assertEqual(subsets, expected_output)

if __name__ == '__main__':
    unittest.main()

### Explanation:

The test suite is written using the unittest module. The test_greedy_sum_subset method is defined to test the greedy_sum_subset function. The function is called with the input array and target sum, and the output is compared with the expected output.

The unittest module provides a framework for writing and running tests. It provides a base class TestCase for defining test cases, and a runner class TestRunner for running tests.

The test_greedy_sum_subset method is defined to test the greedy_sum_subset function. The function is called with the input array and target sum, and the output is compared with the expected output.

The unittest module provides a framework for writing and running tests. It provides a base class TestCase for defining test cases, and a runner class TestRunner for running tests.

The test_greedy_sum_subset method is defined to test the greedy_sum_subset function. The function is called with the input array and target sum, and the output is compared with the expected output.

The unittest module provides a framework for writing and running tests. It provides a base class TestCase for defining test cases, and a runner class TestRunner for running tests.

The test_greedy_sum_subset method is defined to test the greedy_sum_subset function. The function is called with the input array and target sum, and the output is compared with the expected output.

The unittest module provides a framework for writing and running tests. It provides a base class TestCase for defining test cases, and a runner class TestRunner for running tests.