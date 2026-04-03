```python
import unittest

class Test(unittest.TestCase):
    def test_transform_array_after_operations(self):
        self.assertEqual(transform_array_after_operations([-4, 0, -1, 0], 2), [0, 4, 3, 4])
        self.assertEqual(transform_array_after_operations([0, -1, 0, 0, -1, -1, -1, -1, 1, -1], 1), [1, 2, 1, 1, 2, 2, 2, 2, 0, 2])
        self.assertEqual(transform_array_after_operations([0, -1, 0, 0, -1, -1, -1, -1, 1, -1], 2), [1, 2, 1, 1, 2, 2, 2, 2, 0, 2])
        self.assertEqual(transform_array_after_operations([0, -1, 0, 0, -1, -1, -1, -1, 1, -1], 3), [1, 2, 1, 1, 2, 2, 2, 2, 0, 2])
        self.assertEqual(transform_array_after_operations([0, -1, 0, 0, -1, -1, -1, -1, 1, -1], 4), [1, 2, 1, 1, 2, 2, 2, 2, 0, 2])
        self.assertEqual(transform_array_after_operations([0, -1, 0, 0, -1, -1, -1, -1, 1, -1], 5), [1, 2, 1, 1, 2, 2, 2, 2, 0, 2])
        self.assertEqual(transform_array_after_operations([0, -1, 0, 0, -1, -1, -1, -1, 1, -1], 6), [1, 2, 1, 1, 2, 2, 2, 2,