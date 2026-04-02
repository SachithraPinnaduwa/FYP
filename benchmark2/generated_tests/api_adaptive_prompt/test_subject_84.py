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
    def test_normal_case_calculate_fibonacci_number_for_positive_integer(self):
        self.assertEqual(fibonacci(10), 55)

    def test_normal_case_calculate_fibonacci_number_for_large_positive_integer(self):
        self.assertEqual(fibonacci(50), 12586269025)

    def test_edge_case_calculate_fibonacci_number_for_smallest_positive_integer(self):
        self.assertEqual(fibonacci(1), 1)

    def test_edge_case_calculate_fibonacci_number_for_second_smallest_positive_integer(self):
        self.assertEqual(fibonacci(2), 1)

    def test_error_handling_handle_case_when_n_is_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_error_handling_handle_case_when_n_is_negative_integer(self):
        self.assertEqual(fibonacci(-5), 0)

if __name__ == '__main__':
    unittest.main()