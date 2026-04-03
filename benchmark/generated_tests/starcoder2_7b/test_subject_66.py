```python
import unittest
import random

class Test(unittest.TestCase):
    def test_generate_matrices(self):
        N = 100000
        diagonal_sums = []
        for _ in range(N):
            matrix = [[(i * 110 + j) % 200 - 100 for j in range(4)] for i in range(4)]
            diagonal_sum = sum(matrix[i][i] for i in range(4))
            diagonal_sums.append(diagonal_sum)
        self.assertEqual(len(diagonal_sums), N)
        self.assertEqual(len(diagonal_sums[0]), 4)
        self.assertEqual(len(diagonal_sums[0][0]), 4)
        self.assertEqual(len(diagonal_sums[0][0][0]), 4)
        self.assertEqual(len(diagonal_sums[0][0][0][0]), 4)
        self.assertEqual(len(diagonal_sums[0][0][0][0][0]), 4)
        self.assertEqual(len(diagonal_sums[0][0][0][0][0][0]), 4)
        self.assertEqual(len(diagonal_sums[0][0][0][0][0][0][0]), 4)
        self.assertEqual(len(diagonal_sums[0][0][0][0][0][0][0][0]), 4)
        self.assertEqual(len(diagonal_sums[0][0][0][0][0][0][0][0][0]), 4)
        self.assertEqual(len(diagonal_sums[0][0][0][0][0][0][0][0][0][0]), 4)
        self.assertEqual(len(diagonal_sums[0][0][0][0][0][0][0][0][0][0][0]), 4)
        self.assertEqual(len(diagonal_sums[0][0][0][0][0][0][0][0][0][0][0][0]), 4)
        self.assertEqual(len(diagonal_sums[0][0][0][0][0][0][0][0][0][0][0][0][0]), 4)
        self.assertEqual(len(diagonal_sums[0][0