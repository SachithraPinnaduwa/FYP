To create a comprehensive unit test suite for the `count_and_indices` function, we need to cover various scenarios including edge cases, typical cases, and worst-case scenarios. Below is the Python unit test suite using the `unittest` framework:

```python
import unittest

def binary_search(arr, target, find_leftmost):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid
            if find_leftmost:
                high = mid - 1
            else:
                low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

def count_and_indices(arr, target):
    left = binary_search(arr, target, True)
    if left == -1:
        return 0, []

    right = binary_search(arr, target, False)
    count = right - left + 1
    indices = [i for i in range(left, right + 1)]
    return count, indices

class TestCountAndIndices(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(count_and_indices([], 5), (0, []))

    def test_target_not_found(self):
        self.assertEqual(count_and_indices([1, 2, 3, 4, 6], 5), (0, []))

    def test_single_occurrence(self):
        self.assertEqual(count_and_indices([1, 2, 3, 4, 5], 5), (1, [4]))

    def test_multiple_occurrences(self):
        self.assertEqual(count_and_indices([1, 2, 3, 3, 3, 4, 5], 3), (3, [2, 3, 4]))

    def test_duplicate_elements(self):
        self.assertEqual(count_and_indices([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 3), (3, [6, 7, 8]))

    def test_large_array(self):
        large_arr = list(range(10**9))
        self.assertEqual(count_and_indices(large_arr, 500000000), (