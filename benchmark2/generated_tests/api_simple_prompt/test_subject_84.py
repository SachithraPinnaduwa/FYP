from subject_84 import *

import unittest

def fibonacci(n):
    if n <= 1:
        return n

    def multiply_matrices(a, b):
        x = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        y = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        z = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        w = a[1][0] * b[0][1] + a[1][1] * b[1][1]
        return [[x, y], [z, w]]

    def power(matrix, n):
        if n <= 1:
            return matrix

        half = power(matrix, n // 2)
        result = multiply_matrices(half, half)

        if n % 2 == 1:
            result = multiply_matrices(result, matrix)

        return result

    matrix = [[1, 1], [1, 0]]
    result = power(matrix, n - 1)
    return result[0][0]

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(11), 89)
        self.assertEqual(fibonacci(12), 144)
        self.assertEqual(fibonacci(13), 233)
        self.assertEqual(fibonacci(14), 377)
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(16), 987)
        self.assertEqual(fibonacci(17), 1597)
        self.assertEqual(fibonacci(18), 2584)
        self.assertEqual(fibonacci(19), 4181)
        self.assertEqual(fibonacci(20), 6765)

if __name__ == '__main__':
    unittest.main()