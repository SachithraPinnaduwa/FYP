import unittest

def transform_array_after_operations(a, k):
    li = []
    for i in range(k):
        m = max(a)
        a = [m - i for i in a]
        if a in li:
            if not k % 2:
                return li[-1]
            return a
        li.append(a)
    return a

class TestTransformArrayAfterOperations(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(transform_array_after_operations([-4, 0, -1, 0], 2), [0, 4, 3, 4])

    def test_case_2(self):
        self.assertEqual(transform_array_after_operations([0, -1, 0, 0, -1, -1, -1, -1, 1, -1], 1), [1, 2, 1, 1, 2, 2, 2, 2, 0, 2])

    def test_case_3(self):
        self.assertEqual(transform_array_after_operations([2, 2, 2, 2, 2], 5), [0, 0, 0, 0, 0])

    def test_case_4(self):
        self.assertEqual(transform_array_after_operations([-100, -200, 0, 100], 1), [200, 300, 100, 0])

    def test_case_5(self):
        self.assertEqual(transform_array_after_operations([5, 5, 5, 5], 4), [0, 0, 0, 0])

    def test_case_6(self):
        self.assertEqual(transform_array_after_operations([-1, -2, -3], 3), [2, 1, 0])

    def test_case_7(self):
        self.assertEqual(transform_array_after_operations([1, 1, 1, 1], 100000), [0, 0, 0, 0])

    def test_case_8(self):
        self.assertEqual(transform_array_after_operations([100, 200, 300], 2), [100, 100, 100])

    def test_case_9(self):
        self.assertEqual(transform_array_after_operations([0, 0, 0, 0], 1), [0, 0, 0, 0])

    def test_case_10(self):
        self.assertEqual(transform_array_after_operations([-1, 1, -1, 1], 2), [0, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()