import unittest
import math

class TestTriangle(unittest.TestCase):
    def test_is_right_triangle(self):
        self.assertEqual(is_right_triangle(3, 4, 5), True)
        self.assertEqual(is_right_triangle(3, 4, 6), False)
        self.assertEqual(is_right_triangle(3, 5, 6), False)
        self.assertEqual(is_right_triangle(3, 3, 3), False)
        self.assertEqual(is_right_triangle(3, 3, 4), False)
        self.assertEqual(is_right_triangle(3, 4, 4), False)
        self.assertEqual(is_right_triangle(3, 4, 3), False)
        self.assertEqual(is_right_triangle(3, 3, 4), False)
        self.assertEqual(is_right_triangle(3, 4, 3), False)
        self.assertEqual(is_right_triangle(3, 3, 4), False)
        self.assertEqual(is_right_triangle(3, 4, 3), False)
        self.assertEqual(is_right_triangle(3, 3, 4), False)
        self.assertEqual(is_right_triangle(3, 4, 3), False)
        self.assertEqual(is_right_triangle(3, 3, 4), False)
        self.assertEqual(is_right_triangle(3, 4, 3), False)
        self.assertEqual(is_right_triangle(3, 3, 4), False)
        self.assertEqual(is_right_triangle(3, 4, 3), False)
        self.assertEqual(is_right_triangle(3, 3, 4), False)
        self.assertEqual(is_right_triangle(3, 4, 3), False)
        self.assertEqual(is_right_triangle(3, 3, 4), False)
        self.assertEqual(is_right_triangle(3, 4, 3), False)
        self.assertEqual(is_right_triangle(3, 3, 4), False)
        self.assertEqual(is_right_triangle(3, 4, 3), False)