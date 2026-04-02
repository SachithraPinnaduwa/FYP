To write a comprehensive Python unit test suite for the provided code, we need to create multiple test cases that cover various scenarios, including edge cases. Below is the complete unit test suite using the `unittest` framework.

```python
import unittest
from your_module import count_subarrays_with_sum  # Replace 'your_module' with the actual module name where the function is defined

class TestCountSubarraysWithSum(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(count_subarrays_with_sum([], 0), 0)

    def test_zero_sum(self):
        self.assertEqual(count_subarrays_with_sum([0, 0, 0], 0), 6)
        self.assertEqual(count_subarrays_with_sum([1, 0, 1, 0, 1], 0), 4)
        self.assertEqual(count_subarrays_with_sum([1, 1, 1, 1], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(count_subarrays_with_sum([0], 0), 0)
        self.assertEqual(count_subarrays_with_sum([1], 0), 0)
        self.assertEqual(count_subarrays_with_sum([0], 1), 0)
        self.assertEqual(count_subarrays_with_sum([1], 1), 1)

    def test_sums_equal_to_array_length(self):
        self.assertEqual(count_subarrays_with_sum([1, 1, 1, 1], 4), 1)
        self.assertEqual(count_subarrays_with_sum([1, 0, 1, 0, 1], 5), 1)

    def test_large_array(self):
        A = [1] * 10000
        self.assertEqual(count_subarrays_with_sum(A, 10000), 1)
        A = [0] * 10000
        self.assertEqual(count_subarrays_with_sum(A, 0), 5000 * 5001)

    def test_mixed_elements(self):
        self.assertEqual(count_subarrays_with_sum([1, 0, 1, 0, 1], 2), 4)
        self.assertEqual(count_subarrays_with_sum([1, 0, 1, 0, 1], 1), 3)
        self.assertEqual(count_subarrays_with_sum([1, 0, 1, 0, 1], 3), 0)